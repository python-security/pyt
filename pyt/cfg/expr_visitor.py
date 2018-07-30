import ast

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
    ConnectToExitNode,
    EntryOrExitNode,
    IgnoredNode,
    Node,
    RestoreNode,
    ReturnNode,
    YieldNode
)
from .expr_visitor_helper import (
    BUILTINS,
    return_connection_handler,
    SavedVariable
)
from ..helper_visitors import (
    LabelVisitor,
    RHSVisitor
)
from .stmt_visitor import StmtVisitor
from .stmt_visitor_helper import CALL_IDENTIFIER


class ExprVisitor(StmtVisitor):
    def __init__(
        self,
        node,
        project_modules,
        local_modules,
        filename,
        module_definitions=None,
        allow_local_directory_imports=True
    ):
        """Create an empty CFG."""
        super().__init__(allow_local_directory_imports=allow_local_directory_imports)
        self.project_modules = project_modules
        self.local_modules = local_modules if self._allow_local_modules else []
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
        label = LabelVisitor()
        label.visit(node)

        if node.value is None:
            rhs_visitor_result = []
        else:
            rhs_visitor_result = RHSVisitor.result_for_node(node.value)

        # Yield is a bit like augmented assignment to a return value
        this_function_name = self.function_return_stack[-1]
        LHS = 'yld_' + this_function_name
        return self.append_node(YieldNode(
            LHS + ' += ' + label.result,
            LHS,
            node,
            rhs_visitor_result + [LHS],
            path=self.filenames[-1])
        )

    def visit_YieldFrom(self, node):
        return self.visit_Yield(node)

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
        return IgnoredNode()

    def visit_Subscript(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def visit_Tuple(self, node):
        return self.visit_miscelleaneous_node(
            node
        )

    def connect_if_allowed(
        self,
        previous_node,
        node_to_connect_to
    ):
        # e.g.
        # while x != 10:
        #     if x > 0:
        #         print(x)
        #         break
        #     else:
        #         print('hest')
        # print('next')  # self.nodes[-1] is print('hest')
        #
        # So we connect to `while x!= 10` instead
        if self.last_control_flow_nodes[-1]:
            self.last_control_flow_nodes[-1].connect(node_to_connect_to)
            self.last_control_flow_nodes[-1] = None
            return

        # Except in this case:
        #
        # if not image_name:
        #     return 404
        # print('foo')  # We do not want to connect this line with `return 404`
        if previous_node is not self.prev_nodes_to_avoid[-1] and not isinstance(previous_node, ReturnNode):
            previous_node.connect(node_to_connect_to)

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
            self.connect_if_allowed(previous_node, saved_scope_node)

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
            self.connect_if_allowed(self.nodes[-1], restore_node)
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
        self.connect_if_allowed(previous_node, entry_node)

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

        Note: We do not need connect_if_allowed because of the
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
        if any(isinstance(node, YieldNode) for node in function_nodes):
            # Presence of a `YieldNode` means that the function is a generator
            rhs_prefix = 'yld_'
        elif any(isinstance(node, ConnectToExitNode) for node in function_nodes):
            # Only `Return`s and `Raise`s can be of type ConnectToExitNode
            rhs_prefix = 'ret_'
        else:
            return  # No return value

        # Create e.g. ~call_1 = ret_func_foo RestoreNode
        LHS = CALL_IDENTIFIER + 'call_' + str(saved_function_call_index)
        RHS = rhs_prefix + get_call_names_as_string(call_node.func)
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
