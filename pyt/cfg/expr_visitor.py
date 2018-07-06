import ast
import itertools

from .alias_helper import handle_aliases_in_calls
from ..core.ast_helper import (
    Arguments,
    get_call_names_as_string
)
from ..core.module_definitions import ModuleDefinitions
from ..core.node_types import (
    AssignmentCallNode,
    AssignmentNode,
    BBorBInode,
    BoolOpNode,
    ConnectToExitNode,
    ControlFlowExpr,
    EntryOrExitNode,
    IfExpNode,
    IgnoredNode,
    Node,
    RestoreNode,
    ReturnNode,
    StrNode
)
from .expr_visitor_helper import (
    BUILTINS,
    CALL_IDENTIFIER,
    ConnectExpressions,
    connect_expressions,
    get_last_expressions,
    return_connection_handler,
    SavedVariable
)
from ..helper_visitors import (
    LabelVisitor,
    RHSVisitor,
    VarsVisitor
)
from .stmt_visitor import StmtVisitor
from .stmt_visitor_helper import get_first_node


class ExprVisitor(StmtVisitor):
    def __init__(
        self,
        node,
        project_modules,
        local_modules,
        filename,
        module_definitions=None
    ):
        """Create an empty CFG."""
        self.project_modules = project_modules
        self.local_modules = local_modules
        self.filenames = [filename]
        self.blackbox_assignments = set()
        self.nodes = list()
        self.function_call_index = 0
        self.undecided = False
        self.function_names = list()
        self.function_return_stack = list()
        self.module_definitions_stack = list()
        self.prev_nodes_to_avoid = list()
        self.last_control_flow_nodes = list()

        # Are we already in a module?
        if module_definitions:
            self.init_function_cfg(node, module_definitions)
        else:
            self.init_cfg(node)

    def expr_star_handler(
        self,
        exprs
    ):
        """Handle expr* in an AST node.

        Links all expressions together in a list of expressions.
        Makes last_expressions the last_expressions of all exprs combined.
        This code is quite similar to stmt_star_handler in stmt_visitor.py
        """
        if not exprs:
            return ConnectExpressions()

        cfg_expressions = list()
        variables = list()
        visual_variables = list()
        first_node = None
        node_not_to_step_past = self.nodes[-1]

        for expr in exprs:
            node = self.visit(expr)

            if isinstance(node, AssignmentNode):
                # Append str
                variables.append(node.left_hand_side)
                visual_variables.append(node.left_hand_side)
            elif isinstance(node, (ControlFlowExpr, StrNode)):
                # Extend a list
                variables.extend(node.variables)
                visual_variables.append(node.visual_variables)
            else:
                print(f'exprs are {exprs}')
                print(f'expr is {expr}')
                print(f'type of node is {type(node)}')

                vv = VarsVisitor()
                vv.visit(expr)
                variables.extend(vv.result)

                label = LabelVisitor()
                label.visit(expr)
                visual_variables.append(label.result)

            if not isinstance(node, StrNode):
                cfg_expressions.append(node)
                if not first_node:
                    if isinstance(node, ControlFlowExpr):
                        first_node = node.test
                    else:
                        first_node = get_first_node(
                            node,
                            node_not_to_step_past
                        )
                    # Here we connect the first node, to the [-1] node before all the visiting happened
                    node_not_to_step_past.connect(first_node)

        connect_expressions(cfg_expressions)

        return ConnectExpressions(
            first_expression=first_node,
            all_expressions=cfg_expressions,
            last_expressions=get_last_expressions(cfg_expressions) if cfg_expressions else [],
            variables=variables,
            visual_variables=visual_variables
        )

    def init_cfg(self, node):
        self.module_definitions_stack.append(ModuleDefinitions(filename=self.filenames[-1]))

        entry_node = self.append_node(EntryOrExitNode('Entry module'))

        module_statements = self.visit(node)

        if not module_statements:
            raise Exception('Empty module. It seems that your file is empty,' +
                            'there is nothing to analyse.')

        exit_node = self.append_node(EntryOrExitNode('Exit module'))

        if isinstance(module_statements, IgnoredNode):
            entry_node.connect(exit_node)
            return

        first_node = module_statements.first_statement

        if CALL_IDENTIFIER not in first_node.label:
            entry_node.connect(first_node)

        last_nodes = module_statements.last_statements
        exit_node.connect_predecessors(last_nodes)

    def init_function_cfg(self, node, module_definitions):
        self.module_definitions_stack.append(module_definitions)

        self.function_names.append(node.name)
        self.function_return_stack.append(node.name)

        entry_node = self.append_node(EntryOrExitNode('Entry function'))

        module_statements = self.stmt_star_handler(node.body)
        exit_node = self.append_node(EntryOrExitNode('Exit function'))

        if isinstance(module_statements, IgnoredNode):
            entry_node.connect(exit_node)
            return

        first_node = module_statements.first_statement

        if CALL_IDENTIFIER not in first_node.label:
            entry_node.connect(first_node)

        last_nodes = module_statements.last_statements
        exit_node.connect_predecessors(last_nodes)

    def visit_Yield(self, node):
        """
            Yield(expr? value)
        """
        label = LabelVisitor()
        label.visit(node)

        try:
            rhs_visitor = RHSVisitor()
            rhs_visitor.visit(node.value)
        except AttributeError:
            rhs_visitor.result = 'EmptyYield'

        this_function_name = self.function_return_stack[-1]
        LHS = 'yield_' + this_function_name
        return self.append_node(ReturnNode(
            LHS + ' = ' + label.result,
            LHS,
            node,
            rhs_visitor.result,
            path=self.filenames[-1])
        )

    def visit_Attribute(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_Name(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_NameConstant(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_Str(self, node):
        label = LabelVisitor()
        label.visit(node)
        return StrNode(label.result)

    def visit_Subscript(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_Tuple(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_Compare(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_BoolOp(self, node):
        """
            BoolOp(boolop op, expr* values)

            op (And | Or)
            `and` means we might return the one on the right
            `or` means we might return any value

            Consecutive operations with the same operator,
                e.g. a or b or c, are collapsed into one node
                with several values.
        """
        is_or = isinstance(node.op, ast.Or)
        op_str = 'or' if is_or else 'and'

        boolop = self.append_node(BoolOpNode(
            op_str,
            node,
            path=self.filenames[-1]
        ))

        print(f'boolop is {boolop}')

        values = self.expr_star_handler(node.values)

        last_expressions = values.all_expressions if is_or else values.last_expressions

        visual_variables = ' {} '.format(op_str).join(
            values.visual_variables
        )

        variables = list()
        for expr in last_expressions:
            if isinstance(expr, AssignmentNode):
                variables.append(expr.left_hand_side)
            elif isinstance(expr, ControlFlowExpr):
                variables.extend(expr.variables)
            else:
                variables.append(expr.label)

        print(f'variables are now {variables}')
        print(f'last_expressions are {last_expressions}')
        print(f'visual_variables are now {visual_variables}')
        import ipdb
        ipdb.set_trace()
        print('uh oh, last_expressions is wrong')
        return ControlFlowExpr(
            test=boolop,
            last_expressions=last_expressions,
            variables=variables,
            visual_variables=visual_variables
        )

    def visit_keyword(self, node):
        """
             (identifier? arg, expr value)
             NULL identifier for **kwargs
        """
        return self.visit(node.value)

    def visit_IfExp(self, node):
        """
            IfExp(expr test, expr body, expr orelse)
        """
        test = self.append_node(IfExpNode(
            node.test,
            node,
            path=self.filenames[-1]
        ))

        body = self.visit(node.body)

        last_expressions = list()
        # todo: Make this DRY
        if isinstance(body, ControlFlowExpr):
            test.connect(body.test)
            last_expressions.append(orelse.last_expressions)
        if isinstance(body, StrNode):
            pass
        else:
            test.connect(body)
            last_expressions.append(body)

        orelse = self.visit(node.orelse)
        print(f'So orelse is {orelse}')

        if isinstance(orelse, ControlFlowExpr):
            test.connect(orelse.test)
            last_expressions.extend(orelse.last_expressions)
        elif isinstance(orelse, StrNode):
            pass
        else:
            test.connect(orelse)
            last_expressions.append(orelse)


        variables = list()

        for expr in last_expressions:
            if isinstance(expr, AssignmentNode):
                variables.append(expr.left_hand_side)
            elif isinstance(expr, ControlFlowExpr):
                variables.extend(expr.variables)
            else:
                variables.append(expr.label)

        visual_variables = '{} if {} else {}'.format(
            *list(
                map(
                    lambda expr: expr.left_hand_side if isinstance(expr, AssignmentNode) else expr.visual_variables if isinstance(expr, ControlFlowExpr) else expr.label,
                    [body, test, orelse]
                )
            )
        )
        print(f'the last_expressions are {last_expressions}')
        print(f'the variables are {variables}')
        import ipdb
        ipdb.set_trace()

        return ControlFlowExpr(
            test=test,
            last_expressions=last_expressions,
            variables=variables,
            visual_variables=visual_variables
        )

    # def connect_if_allowed(
    #     self,
    #     previous_node,
    #     node_to_connect_to
    # ):
    #     # e.g.
    #     # while x != 10:
    #     #     if x > 0:
    #     #         print(x)
    #     #         break
    #     #     else:
    #     #         print('hest')
    #     # print('next')  # self.nodes[-1] is print('hest')
    #     #
    #     # So we connect to `while x!= 10` instead
    #     if self.last_control_flow_nodes[-1]:
    #         self.last_control_flow_nodes[-1].connect(node_to_connect_to)
    #         self.last_control_flow_nodes[-1] = None
    #         return

    #     # Except in this case:
    #     #
    #     # if not image_name:
    #     #     return 404
    #     # print('foo')  # We do not want to connect this line with `return 404`
    #     if previous_node is not self.prev_nodes_to_avoid[-1] and not isinstance(previous_node, ReturnNode):
    #         previous_node.connect(node_to_connect_to)

    def save_local_scope(
        self,
        line_number,
        saved_function_call_index
    ):
        """Save the local scope before entering a function call by saving all the LHS's of assignments so far.

        Args:
            line_number(int): Of the def of the function call about to be entered into.
            saved_function_call_index(int): Unique number for each call.

        Returns:
            saved_variables(list[SavedVariable])
            first_node(EntryOrExitNode or None or RestoreNode): Used to connect previous statements to this function.
        """
        saved_variables = list()
        saved_variables_so_far = set()
        first_node = None

        # Make e.g. save_N_LHS = assignment.LHS for each AssignmentNode
        for assignment in [node for node in self.nodes
                           if (type(node) == AssignmentNode or
                               type(node) == AssignmentCallNode or
                               type(Node) == BBorBInode)]:  # type() is used on purpose here
            if assignment.left_hand_side in saved_variables_so_far:
                continue
            saved_variables_so_far.add(assignment.left_hand_side)
            save_name = 'save_{}_{}'.format(saved_function_call_index, assignment.left_hand_side)

            previous_node = self.nodes[-1]

            saved_scope_node = RestoreNode(
                save_name + ' = ' + assignment.left_hand_side,
                save_name,
                [assignment.left_hand_side],
                line_number=line_number,
                path=self.filenames[-1]
            )
            if not first_node:
                first_node = saved_scope_node

            self.nodes.append(saved_scope_node)
            # Save LHS
            saved_variables.append(SavedVariable(LHS=save_name,
                                                 RHS=assignment.left_hand_side))
            # self.connect_if_allowed(previous_node, saved_scope_node)

        return (saved_variables, first_node)

    def save_def_args_in_temp(
        self,
        call_args,
        def_args,
        line_number,
        saved_function_call_index,
        first_node
    ):
        """Save the arguments of the definition being called. Visit the arguments if they're calls.

        Args:
            call_args(list[ast.Name]): Of the call being made.
            def_args(ast_helper.Arguments): Of the definition being called.
            line_number(int): Of the call being made.
            saved_function_call_index(int): Unique number for each call.
            first_node(EntryOrExitNode or None or RestoreNode): Used to connect previous statements to this function.

        Returns:
            args_mapping(dict): A mapping of call argument to definition argument.
            first_node(EntryOrExitNode or None or RestoreNode): Used to connect previous statements to this function.
        """
        args_mapping = dict()
        last_return_value_of_nested_call = None

        # Create e.g. temp_N_def_arg1 = call_arg1_label_visitor.result for each argument
        for i, call_arg in enumerate(call_args):
            # If this results in an IndexError it is invalid Python
            def_arg_temp_name = 'temp_' + str(saved_function_call_index) + '_' + def_args[i]

            return_value_of_nested_call = None
            if isinstance(call_arg, ast.Call):
                return_value_of_nested_call = self.visit(call_arg)
                restore_node = RestoreNode(
                    def_arg_temp_name + ' = ' + return_value_of_nested_call.left_hand_side,
                    def_arg_temp_name,
                    [return_value_of_nested_call.left_hand_side],
                    line_number=line_number,
                    path=self.filenames[-1]
                )
                if return_value_of_nested_call in self.blackbox_assignments:
                    self.blackbox_assignments.add(restore_node)
            elif isinstance(call_arg, ast.BoolOp):
                print('Handle me')
            elif isinstance(call_arg, ast.IfExp):
                print('Handle me')
            else:
                call_arg_label_visitor = LabelVisitor()
                call_arg_label_visitor.visit(call_arg)
                call_arg_rhs_visitor = RHSVisitor()
                call_arg_rhs_visitor.visit(call_arg)
                restore_node = RestoreNode(
                    def_arg_temp_name + ' = ' + call_arg_label_visitor.result,
                    def_arg_temp_name,
                    call_arg_rhs_visitor.result,
                    line_number=line_number,
                    path=self.filenames[-1]
                )

            # If there are no saved variables, then this is the first node
            if not first_node:
                first_node = restore_node

            if isinstance(call_arg, ast.Call):
                if last_return_value_of_nested_call:
                    # connect inner to other_inner in e.g. `outer(inner(image_name), other_inner(image_name))`
                    if isinstance(return_value_of_nested_call, BBorBInode):
                        last_return_value_of_nested_call.connect(return_value_of_nested_call)
                    else:
                        last_return_value_of_nested_call.connect(return_value_of_nested_call.first_node)
                else:
                    # I should only set this once per loop, inner in e.g. `outer(inner(image_name), other_inner(image_name))`
                    # (inner_most_call is used when predecessor is a ControlFlowNode in connect_control_flow_node)
                    if isinstance(return_value_of_nested_call, BBorBInode):
                        first_node.inner_most_call = return_value_of_nested_call
                    else:
                        first_node.inner_most_call = return_value_of_nested_call.first_node
                # We purposefully should not set this as the first_node of return_value_of_nested_call, last makes sense
                last_return_value_of_nested_call = return_value_of_nested_call
            # self.connect_if_allowed(self.nodes[-1], restore_node)
            self.nodes.append(restore_node)

            if isinstance(call_arg, ast.Call):
                args_mapping[return_value_of_nested_call.left_hand_side] = def_args[i]
            else:
                args_mapping[def_args[i]] = call_arg_label_visitor.result

        return (args_mapping, first_node)

    def create_local_scope_from_def_args(
        self,
        call_args,
        def_args,
        line_number,
        saved_function_call_index
    ):
        """Create the local scope before entering the body of a function call.

        Args:
            call_args(list[ast.Name]): Of the call being made.
            def_args(ast_helper.Arguments): Of the definition being called.
            line_number(int): Of the def of the function call about to be entered into.
            saved_function_call_index(int): Unique number for each call.

        Note: We do not need a connect_if_allowed because of the
              preceding call to save_def_args_in_temp.
        """
        # Create e.g. def_arg1 = temp_N_def_arg1 for each argument
        for i in range(len(call_args)):
            def_arg_local_name = def_args[i]
            def_arg_temp_name = 'temp_' + str(saved_function_call_index) + '_' + def_args[i]
            local_scope_node = RestoreNode(
                def_arg_local_name + ' = ' + def_arg_temp_name,
                def_arg_local_name,
                [def_arg_temp_name],
                line_number=line_number,
                path=self.filenames[-1]
            )
            # Chain the local scope nodes together
            self.nodes[-1].connect(local_scope_node)
            self.nodes.append(local_scope_node)

    def visit_and_get_function_nodes(
        self,
        definition,
        first_node
    ):
        """Visits the nodes of a user defined function.

        Args:
            definition(LocalModuleDefinition): Definition of the function being added.
            first_node(EntryOrExitNode or None or RestoreNode): Used to connect previous statements to this function.

        Returns:
            the_new_nodes(list[Node]): The nodes added while visiting the function.
            first_node(EntryOrExitNode or None or RestoreNode): Used to connect previous statements to this function.
        """
        len_before_visiting_func = len(self.nodes)
        previous_node = self.nodes[-1]
        entry_node = self.append_node(EntryOrExitNode('Function Entry ' +
                                                      definition.name))
        if not first_node:
            first_node = entry_node
        # self.connect_if_allowed(previous_node, entry_node)

        function_body_connect_statements = self.stmt_star_handler(definition.node.body)
        entry_node.connect(function_body_connect_statements.first_statement)

        exit_node = self.append_node(EntryOrExitNode('Exit ' + definition.name))
        exit_node.connect_predecessors(function_body_connect_statements.last_statements)

        the_new_nodes = self.nodes[len_before_visiting_func:]
        return_connection_handler(the_new_nodes, exit_node)

        return (the_new_nodes, first_node)

    def restore_saved_local_scope(
        self,
        saved_variables,
        args_mapping,
        line_number
    ):
        """Restore the previously saved variables to their original values.

        Args:
           saved_variables(list[SavedVariable])
           args_mapping(dict): A mapping of call argument to definition argument.
           line_number(int): Of the def of the function call about to be entered into.

        Note: We do not need connect_if_allowed for the [-1].connect because of the
              preceding call to save_local_scope.
        """
        restore_nodes = list()
        for var in saved_variables:
            # Is var.RHS a call argument?
            if var.RHS in args_mapping:
                # If so, use the corresponding definition argument for the RHS of the label.
                restore_nodes.append(RestoreNode(
                    var.RHS + ' = ' + args_mapping[var.RHS],
                    var.RHS,
                    [var.LHS],
                    line_number=line_number,
                    path=self.filenames[-1]
                ))
            else:
                # Create a node for e.g. foo = save_1_foo
                restore_nodes.append(RestoreNode(
                    var.RHS + ' = ' + var.LHS,
                    var.RHS,
                    [var.LHS],
                    line_number=line_number,
                    path=self.filenames[-1]
                ))

        # Chain the restore nodes
        for node, successor in zip(restore_nodes, restore_nodes[1:]):
            node.connect(successor)

        if restore_nodes:
            # Connect the last node to the first restore node
            self.nodes[-1].connect(restore_nodes[0])
            self.nodes.extend(restore_nodes)

        return restore_nodes

    def return_handler(
        self,
        call_node,
        function_nodes,
        saved_function_call_index,
        first_node
    ):
        """Handle the return from a function during a function call.

        Args:
            call_node(ast.Call) : The node that calls the definition.
            function_nodes(list[Node]): List of nodes of the function being called.
            saved_function_call_index(int): Unique number for each call.
            first_node(EntryOrExitNode or RestoreNode): Used to connect previous statements to this function.
        """
        for node in function_nodes:
            # Only `Return`s and `Raise`s can be of type ConnectToExitNode
            if isinstance(node, ConnectToExitNode):
                # Create e.g. ~call_1 = ret_func_foo RestoreNode
                LHS = CALL_IDENTIFIER + 'call_' + str(saved_function_call_index)
                RHS = 'ret_' + get_call_names_as_string(call_node.func)
                return_node = RestoreNode(
                    LHS + ' = ' + RHS,
                    LHS,
                    [RHS],
                    line_number=call_node.lineno,
                    path=self.filenames[-1]
                )
                return_node.first_node = first_node

                self.nodes[-1].connect(return_node)
                self.nodes.append(return_node)
                return

    def process_function(self, call_node, definition):
        """Processes a user defined function when it is called.

        Increments self.function_call_index each time it is called, we can refer to it as N in the comments.
        Make e.g. save_N_LHS = assignment.LHS for each AssignmentNode. (save_local_scope)
        Create e.g. temp_N_def_arg1 = call_arg1_label_visitor.result for each argument.
            Visit the arguments if they're calls. (save_def_args_in_temp)
        Create e.g. def_arg1 = temp_N_def_arg1 for each argument. (create_local_scope_from_def_args)
        Visit and get function nodes. (visit_and_get_function_nodes)
        Loop through each save_N_LHS node and create an e.g.
            foo = save_1_foo or, if foo was a call arg, foo = arg_mapping[foo]. (restore_saved_local_scope)
        Create e.g. ~call_1 = ret_func_foo RestoreNode. (return_handler)

        Notes:
            Page 31 in the original thesis, but changed a little.
            We don't have to return the ~call_1 = ret_func_foo RestoreNode made in return_handler,
                because it's the last node anyway, that we return in this function.
            e.g. ret_func_foo gets assigned to visit_Return.

        Args:
            call_node(ast.Call) : The node that calls the definition.
            definition(LocalModuleDefinition): Definition of the function being called.

        Returns:
            Last node in self.nodes, probably the return of the function appended to self.nodes in return_handler.
        """
        self.function_call_index += 1
        saved_function_call_index = self.function_call_index

        def_node = definition.node

        saved_variables, first_node = self.save_local_scope(
            def_node.lineno,
            saved_function_call_index
        )

        args_mapping, first_node = self.save_def_args_in_temp(
            call_node.args,
            Arguments(def_node.args),
            call_node.lineno,
            saved_function_call_index,
            first_node
        )
        self.filenames.append(definition.path)
        self.create_local_scope_from_def_args(
            call_node.args,
            Arguments(def_node.args),
            def_node.lineno,
            saved_function_call_index
        )
        function_nodes, first_node = self.visit_and_get_function_nodes(
            definition,
            first_node
        )
        self.filenames.pop()  # Should really probably move after restore_saved_local_scope!!!
        self.restore_saved_local_scope(
            saved_variables,
            args_mapping,
            def_node.lineno
        )
        self.return_handler(
            call_node,
            function_nodes,
            saved_function_call_index,
            first_node
        )
        self.function_return_stack.pop()

        return self.nodes[-1]

    def add_blackbox_or_builtin_call(self, node, blackbox):
        """Processes a blackbox or builtin function when it is called.
        Nothing gets assigned to ret_func_foo in the builtin/blackbox case.

        Increments self.function_call_index each time it is called, we can refer to it as N in the comments.
        Create e.g. ¤call_1 = ret_func_foo RestoreNode.

        Create e.g. temp_N_def_arg1 = call_arg1_label_visitor.result for each argument.
        Visit the arguments if they're calls. (save_def_args_in_temp)

        I do not think I care about this one actually -- Create e.g. def_arg1 = temp_N_def_arg1 for each argument.
        (create_local_scope_from_def_args)

        Add RestoreNode to the end of the Nodes.

        Args:
            node(ast.Call) : The node that calls the definition.
            blackbox(bool): Whether or not it is a builtin or blackbox call.
        Returns:
            call_node(BBorBInode): The call node.
        """
        self.function_call_index += 1
        saved_function_call_index = self.function_call_index
        self.undecided = False

        call_label = LabelVisitor()
        call_label.visit(node)

        index = call_label.result.find('(')

        # Create e.g. ¤call_1 = ret_func_foo
        LHS = CALL_IDENTIFIER + 'call_' + str(saved_function_call_index)

        call_node = BBorBInode(
            left_hand_side=LHS,
            line_number=node.lineno,
            path=self.filenames[-1],
            func_name=call_label.result[:index]
        )

        # Maybe I can remove the ignored nodes and add them to my visual args?
        # Who knows?
        connected_expressions = self.expr_star_handler(list(itertools.chain(
            node.args,
            node.keywords
        )))
        print(f'\n\n\n\n\n\n\nsomething IS {connected_expressions}')
        print(f'connected_expressions.variables are {connected_expressions.variables}\n\n\n\n\n\n\n')
        print('LAST EXPRESSIONS IS ')
        for expr in connected_expressions.last_expressions:
            expr.connect(call_node)

        RHS = 'ret_{}({})'.format(
            call_label.result[:index],
            ', '.join(connected_expressions.visual_variables)
        )
        call_node.label = LHS + ' = ' + RHS

        # .args is only used in get_sink_args
        # We make a new list because right_hand_side_variables is extended in assignment_call_node
        call_node.right_hand_side_variables = connected_expressions.variables
        call_node.args = list(connected_expressions.variables)

        if blackbox:
            self.blackbox_assignments.add(call_node)

        self.nodes.append(call_node)

        return call_node

    def visit_Call(self, node):
        _id = get_call_names_as_string(node.func)
        local_definitions = self.module_definitions_stack[-1]

        alias = handle_aliases_in_calls(_id, local_definitions.import_alias_mapping)
        if alias:
            definition = local_definitions.get_definition(alias)
        else:
            definition = local_definitions.get_definition(_id)

        # e.g. "request.args.get" -> "get"
        last_attribute = _id.rpartition('.')[-1]

        if definition:
            if isinstance(definition.node, ast.ClassDef):
                self.add_blackbox_or_builtin_call(node, blackbox=False)
            elif isinstance(definition.node, ast.FunctionDef):
                self.undecided = False
                self.function_return_stack.append(_id)
                return self.process_function(node, definition)
            else:
                raise Exception('Definition was neither FunctionDef or ' +
                                'ClassDef, cannot add the function ')
        elif last_attribute not in BUILTINS:
            # Mark the call as a blackbox because we don't have the definition
            return self.add_blackbox_or_builtin_call(node, blackbox=True)
        return self.add_blackbox_or_builtin_call(node, blackbox=False)
