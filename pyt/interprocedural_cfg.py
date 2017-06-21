import ast
import os.path
from collections import namedtuple

from .alias_helper import (
    as_alias_handler,
    handle_aliases_in_calls,
    handle_aliases_in_init_files,
    handle_fdid_aliases,
    not_as_alias_handler,
    retrieve_import_alias_mapping
)
from .ast_helper import Arguments, generate_ast, get_call_names_as_string
from .base_cfg import (
    AssignmentNode,
    CALL_IDENTIFIER,
    CFG,
    ConnectToExitNode,
    EntryOrExitNode,
    IgnoredNode,
    Node,
    RestoreNode,
    ReturnNode,
    Visitor
)
from .label_visitor import LabelVisitor
from .module_definitions import (
    LocalModuleDefinition,
    ModuleDefinition,
    ModuleDefinitions
)
from .project_handler import get_directory_modules
from .right_hand_side_visitor import RHSVisitor
from pyt.utils.log import enable_logger, logger
enable_logger(to_file='./pyt.log')


SavedVariable = namedtuple('SavedVariable', 'LHS RHS')
NOT_A_BLACKBOX = set(['Flask',
                      'run',
                      'get',
                      'replace',
                      'read',
                      'set_cookie',
                      'make_response',
                      'SQLAlchemy',
                      'Column',
                      'execute',
                      'sessionmaker',
                      'Session',
                      'filter',
                      'execute',
                      'call',
                      'render_template',
                      'redirect',
                      'url_for',
                      'flash',
                      'jsonify'])


class InterproceduralVisitor(Visitor):
    def __init__(self, node, project_modules, local_modules,
                 filename, module_definitions=None):
        """Create an empty CFG."""
        self.project_modules = project_modules
        self.local_modules = local_modules
        self.filenames = [filename]
        self.blackbox_assignments = set()
        self.blackbox_calls = set()
        self.nodes = list()
        self.function_call_index = 0
        self.undecided = False
        self.function_names = list()
        self.function_return_stack = list()
        self.module_definitions_stack = list()

        # Are we already in a module?
        if module_definitions:
            self.init_function_cfg(node, module_definitions)
        else:
            self.init_cfg(node)

    def init_cfg(self, node):
        self.module_definitions_stack.append(ModuleDefinitions(filename=self.filenames[-1]))

        entry_node = self.append_node(EntryOrExitNode("Entry module"))

        module_statements = self.visit(node)

        if not module_statements:
            raise Exception('Empty module. It seems that your file is empty,' +
                            'there is nothing to analyse.')

        if not isinstance(module_statements, IgnoredNode):
            first_node = module_statements.first_statement

            if CALL_IDENTIFIER not in first_node.label:
                entry_node.connect(first_node)

            exit_node = self.append_node(EntryOrExitNode("Exit module"))

            last_nodes = module_statements.last_statements
            exit_node.connect_predecessors(last_nodes)
        else:
            exit_node = self.append_node(EntryOrExitNode("Exit module"))
            entry_node.connect(exit_node)

    def init_function_cfg(self, node, module_definitions):
        logger.debug("Create the CFG for a function")
        self.module_definitions_stack.append(module_definitions)

        self.function_names.append(node.name)
        self.function_return_stack.append(node.name)

        entry_node = self.append_node(EntryOrExitNode("Entry function"))

        module_statements = self.stmt_star_handler(node.body)

        first_node = module_statements.first_statement

        if CALL_IDENTIFIER not in first_node.label:
            entry_node.connect(first_node)

        exit_node = self.append_node(EntryOrExitNode("Exit function"))

        last_nodes = module_statements.last_statements
        exit_node.connect_predecessors(last_nodes)

    def visit_ClassDef(self, node):
        self.add_to_definitions(node)

        local_definitions = self.module_definitions_stack[-1]
        local_definitions.classes.append(node.name)

        parent_definitions = self.get_parent_definitions()
        if parent_definitions:
            parent_definitions.classes.append(node.name)

        self.stmt_star_handler(node.body)

        local_definitions.classes.pop()
        if parent_definitions:
            parent_definitions.classes.pop()

        return IgnoredNode()

    def get_parent_definitions(self):
        parent_definitions = None
        if len(self.module_definitions_stack) > 1:
            parent_definitions = self.module_definitions_stack[-2]
        return parent_definitions

    def visit_FunctionDef(self, node):
        self.add_to_definitions(node)

        return IgnoredNode()

    def add_to_definitions(self, node):
        local_definitions = self.module_definitions_stack[-1]
        parent_definitions = self.get_parent_definitions()

        if parent_definitions:
            parent_qualified_name = '.'.join(parent_definitions.classes +
                                             [node.name])
            parent_definition = ModuleDefinition(parent_definitions,
                                                 parent_qualified_name,
                                                 local_definitions.module_name,
                                                 self.filenames[-1])
            parent_definition.node = node
            parent_definitions.append_if_local_or_in_imports(parent_definition)

        local_qualified_name = '.'.join(local_definitions.classes +
                                        [node.name])
        local_definition = LocalModuleDefinition(local_definitions,
                                                 local_qualified_name,
                                                 None,
                                                 self.filenames[-1])
        local_definition.node = node
        local_definitions.append_if_local_or_in_imports(local_definition)

        self.function_names.append(node.name)

    def return_connection_handler(self, nodes, exit_node):
        """Connect all return statements to the Exit node."""
        for function_body_node in nodes:
            if isinstance(function_body_node, ConnectToExitNode):
                if exit_node not in function_body_node.outgoing:
                    function_body_node.connect(exit_node)

    def visit_Return(self, node):
        label = LabelVisitor()
        label.visit(node)

        this_function_name = self.function_return_stack[-1]

        try:
            rhs_visitor = RHSVisitor()
            rhs_visitor.visit(node.value)
        except AttributeError:
            rhs_visitor.result = 'EmptyReturn'

        LHS = 'ret_' + this_function_name
        return self.append_node(ReturnNode(LHS + ' = ' + label.result,
                                           LHS, rhs_visitor.result,
                                           node, line_number=node.lineno,
                                           path=self.filenames[-1]))

    def visit_Yield(self, node):
        label = LabelVisitor()
        label.visit(node)

        this_function_name = self.function_return_stack[-1]

        try:
            rhs_visitor = RHSVisitor()
            rhs_visitor.visit(node.value)
        except AttributeError:
            rhs_visitor.result = 'EmptyYield'

        LHS = 'yield_' + this_function_name
        return self.append_node(ReturnNode(LHS + ' = ' + label.result,
                                           LHS, rhs_visitor.result,
                                           node, line_number=node.lineno,
                                           path=self.filenames[-1]))

    def save_local_scope(self, line_number):
        """Save the local scope before entering a function call by saving all the LHS's of assignments.

        Args:
            line_number(int): Of the def of the function call about to be entered into.

        Returns:
            saved_variables(list[SavedVariable])
        """
        saved_variables = list()
        previous_node = self.nodes[-1]

        # Make e.g. save_N_LHS = assignment1.LHS for each AssignmentNode
        for assignment in [node for node in self.nodes
                           if type(node) == AssignmentNode]: # type() is used on purpose here
            save_name = 'save_' + str(self.function_call_index) + '_' +\
                        assignment.left_hand_side
            # Save LHS
            saved_variables.append(SavedVariable(LHS=save_name,
                                                 RHS=assignment.left_hand_side))
            saved_scope_node = RestoreNode(save_name + ' = ' + assignment.left_hand_side,
                                           save_name,
                                           [assignment.left_hand_side],
                                           line_number=line_number,
                                           path=self.filenames[-1])
            self.append_node(saved_scope_node)
            # Connect them all to the same Node and not chain them???
            previous_node.connect(saved_scope_node)

        logger.debug("len(saved_variables) is %s", len(saved_variables))
        logger.debug("saved_variables are %s", saved_variables)
        logger.debug("line_number is %s", line_number)
        return saved_variables

    def save_def_args_in_temp(self, call_args, def_args, line_number):
        """Save the arguments of the definition being called.

        Args:
            call_args(list[ast.Name]): Of the call being made.
            def_args(ast_helper.Arguments): Of the definition being called.
            line_number(int): Of the call being made.

        Returns:
            args_mapping(dict): A mapping of call argument to definition argument.
        """
        args_mapping = dict()
        # logger.debug("[FOR COMMENTS] TYPE OF call_args[0] is %s", type(call_args[0]))
        # logger.debug("[FOR COMMENTS] TYPE OF def_args is %s", type(def_args))
        # logger.debug("[FOR COMMENTS] def_args is %s", def_args)

        # Create e.g. temp_N_def_arg1 = call_arg1_label_visitor.result for each argument
        for i, call_arg in enumerate(call_args):
            def_arg_temp_name = 'temp_' + str(self.function_call_index) + '_' + def_args[i]

            call_arg_label_visitor = LabelVisitor()
            call_arg_label_visitor.visit(call_arg)
            call_arg_rhs_visitor = RHSVisitor()
            call_arg_rhs_visitor.visit(call_arg)

            node = RestoreNode(def_arg_temp_name + ' = ' + call_arg_label_visitor.result,
                               def_arg_temp_name,
                               call_arg_rhs_visitor.result,
                               line_number=line_number,
                               path=self.filenames[-1])

            self.nodes[-1].connect(node)
            self.nodes.append(node)

            args_mapping[call_arg_label_visitor.result] = def_args[i]

        logger.debug("[FOR COMMENTS] args_mapping is %s", args_mapping)
        return args_mapping

    def create_local_scope_from_def_args(self,
                                         call_args,
                                         def_args,
                                         line_number):
        """Create the local scope before entering the body of a function call.

        Args:
            call_args(list[ast.Name]): Of the call being made.
            def_args(ast_helper.Arguments): Of the definition being called.
            line_number(int): Of the def of the function call about to be entered into.
        """

        # Create e.g. def_arg1 = temp_N_def_arg1 for each argument
        for i in range(len(call_args)):
            def_arg_local_name = def_args[i]
            def_arg_temp_name = 'temp_' + str(self.function_call_index) + '_' + def_args[i]
            local_scope_node = RestoreNode(def_arg_local_name + ' = ' + def_arg_temp_name,
                                           def_arg_local_name,
                                           [def_arg_temp_name],
                                           line_number=line_number,
                                           path=self.filenames[-1])
            # Chain the local scope nodes together
            previous_node = self.nodes[-1]
            self.append_node(local_scope_node)
            previous_node.connect(local_scope_node)

    def restore_saved_local_scope(self,
                                  saved_variables,
                                  args_mapping,
                                  line_number):
        """Restore the previously saved variables to their original values.

        Args:
           saved_variables(list[SavedVariable])
           args_mapping(dict): A mapping of call argument to definition argument.
           line_number(int): Of the def of the function call about to be entered into.

        Returns:
            restore_nodes(list[RestoreNode]): A list of the nodes that were restored.
        """
        logger.debug("[FOR COMMENTS] args_mapping in restore_saved_local_scope is %s", args_mapping)
        restore_nodes = list()
        for var in saved_variables:
            # Is var.RHS a call argument?
            if var.RHS in args_mapping:
                logger.debug("var.RHS inside of args_mapping is %s", var.RHS)
                # If so, use the corresponding definition argument for the RHS of the label.
                logger.debug("[BIRCH] making a '%s = %s' RestoreNode", var.RHS, args_mapping[var.RHS])
                restore_nodes.append(RestoreNode(var.RHS + ' = ' + args_mapping[var.RHS],
                                                 var.RHS,
                                                 [var.LHS],
                                                 line_number=line_number,
                                                 path=self.filenames[-1]))
            else:
                logger.debug("[2ND BIRCH] making a '%s = %s' RestoreNode", var.RHS, var.LHS)                
                # Create a node for e.g. foo = save_1_foo
                restore_nodes.append(RestoreNode(var.RHS + ' = ' + var.LHS,
                                                 var.RHS,
                                                 [var.LHS],
                                                 line_number=line_number,
                                                 path=self.filenames[-1]))

        # Chain the restore nodes
        for node, successor in zip(restore_nodes, restore_nodes[1:]):
            node.connect(successor)

        if restore_nodes:
            # Connect the last node to the first restore node
            self.nodes[-1].connect(restore_nodes[0])
            self.nodes.extend(restore_nodes)
        logger.debug("[FOR COMMENTS] restore_nodes in restore_saved_local_scope is %s", restore_nodes)
        return restore_nodes

    def return_handler(self, call_node, function_nodes):
        """Handle the return from a function during a function call.
        It doesn't handle multiple returns, at the moment.

        Args:
            call_node(ast.Call) : The node that calls the definition.
            function_nodes(list[Node]): List of nodes of the function being called.

        Returns:
            Last node in self.nodes, probably the return of the function.
        """

        logger.debug("IMPORTANT, in return_handler")
        for node in function_nodes:
            # Only Return's and Raise's can be of type ConnectToExitNode
            if isinstance(node, ConnectToExitNode):
                # logger.debug("PROCESS call_node being processed in return_handler is %s", call_node)
                # logger.debug("PROCESS dir(call_node) being processed in return_handler is %s", dir(call_node))
                # logger.debug("PROCESS dir(call_node.func) being processed in return_handler is %s", dir(call_node.func))
                # logger.debug("PROCESS call_node being processed in return_handler is %s", call_node.func.id)
                
                # Create e.g. ¤call_1 = ret_func_foo RestoreNode
                LHS = CALL_IDENTIFIER + 'call_' + str(self.function_call_index)
                RHS = 'ret_' + get_call_names_as_string(call_node.func)
                return_node = RestoreNode(LHS + ' = ' + RHS,
                                          LHS,
                                          [RHS],
                                          line_number=call_node.lineno,
                                          path=self.filenames[-1])
                previous_node = self.nodes[-1]
                self.append_node(return_node)
                previous_node.connect(return_node)
                break

    def process_function(self, call_node, definition):
        """Processes a user defined function when it is called.

        Args:
            call_node(ast.Call) : The node that calls the definition.
            definition(LocalModuleDefinition): Definition of the function being called.

        Returns:
            Last node in self.nodes, probably the return of the function.
        """

        logger.debug("call_node is %s", call_node)
        logger.debug("type(call_node) is %s", type(call_node))
        try:
            self.function_call_index += 1
            def_node = definition.node

            # FIGURE OUT EVERY LINE OF THIS FUNCTION ESPECIALLY HOW RETURN VALUES WORK
            saved_variables = self.save_local_scope(def_node.lineno)

            args_mapping = self.save_def_args_in_temp(call_node.args,
                                                      Arguments(def_node.args),
                                                      call_node.lineno)

            self.filenames.append(definition.path)
            self.create_local_scope_from_def_args(call_node.args,
                                                  Arguments(def_node.args),
                                                  def_node.lineno)
            function_nodes = self.visit_and_get_function_nodes(definition)
            self.filenames.pop()  # Maybe move after restore nodes
            self.restore_saved_local_scope(saved_variables, args_mapping, def_node.lineno)
            self.return_handler(call_node, function_nodes)
            self.function_return_stack.pop()
            logger.debug("[FOR COMMENTS] last node is %s", self.nodes[-1])
            logger.debug("[FOR COMMENTS] type of last node is %s", type(self.nodes[-1]))

        except IndexError:
            error_call = get_call_names_as_string(call_node.func)
            print('Error: Possible nameclash in "{}".' +
                  ' Call omitted!\n'.format(error_call))

        # logger.debug("[FOR COMMENTS] last node is %s", self.nodes[-1])
        # logger.debug("[FOR COMMENTS] type of last node is %s", type(self.nodes[-1]))

        return self.nodes[-1]

    def visit_and_get_function_nodes(self, definition):
        """Visits the nodes of a user defined function.

        Args:
            definition(LocalModuleDefinition): Definition of the function being added.

        Returns:
            the_new_nodes(list[Node]): The nodes added while visiting the function.
        """
        len_before_visiting_func = len(self.nodes)
        previous_node = self.nodes[-1]
        entry_node = self.append_node(EntryOrExitNode("Function Entry " +
                                                      definition.name))
        previous_node.connect(entry_node)
        function_body_connect_statements = self.stmt_star_handler(definition.node.body)

        entry_node.connect(function_body_connect_statements.first_statement)

        exit_node = self.append_node(EntryOrExitNode("Exit " + definition.name))
        exit_node.connect_predecessors(function_body_connect_statements.last_statements)

        the_new_nodes = self.nodes[len_before_visiting_func:]
        self.return_connection_handler(the_new_nodes, exit_node)

        return the_new_nodes

    def visit_Call(self, node):
        _id = get_call_names_as_string(node.func)
        self.function_return_stack.append(_id)

        local_definitions = self.module_definitions_stack[-1]

        alias = handle_aliases_in_calls(_id, local_definitions.import_alias_mapping)
        if alias:
            definition = local_definitions.get_definition(alias)
        else:
            definition = local_definitions.get_definition(_id)

        logger.debug("_id is %s", _id)
        logger.debug("node is %s", node)
        # logger.debug("dir(node) is %s", dir(node))
        logger.debug("node.func is %s", node.func)
        # logger.debug("dir(node.func) is %s", dir(node.func))
        logger.debug("node.args is %s", node.args)
        # logger.debug("dir(node.args) is %s", dir(node.args))

        # # We can maybe just visit the whole list, let's try each arg first
        # for arg in node.args:
        #     logger.debug("arg is %s", arg)
        #     # logger.debug("arg.s is %s", arg.s)
        #     logger.debug("type(arg) is %s", type(arg))
        #     logger.debug("dir(arg) is %s", dir(arg))
        #     # logger.debug("arg.func is %s", arg.func)
        #     self.visit(arg)
        #     # logger.debug("Result of RHS visitor is %s", rhs_visitor.result)



        # # maybe if "return_of.." is a restore node we do something special!
        # for arg in node.args:
        #     return_of_visit_arg = self.visit(arg)
        #     if isinstance(return_of_visit_arg, RestoreNode):
        #         logger.debug("return_of_visit_arg is %s", return_of_visit_arg)
        #         logger.debug("return_of_visit_arg.right_hand_side_variables is %s", return_of_visit_arg.right_hand_side_variables)
        #         logger.debug("type(return_of_visit_arg) is %s", type(return_of_visit_arg))
        #         logger.debug("dir(return_of_visit_arg) is %s", dir(return_of_visit_arg))

        # for keyword in node.keywords:
        #     return_of_visit_keyword = self.visit(keyword)
        #     logger.debug("return_of_visit_keyword is %s", return_of_visit_keyword)
        #     logger.debug("type(return_of_visit_keyword) is %s", type(return_of_visit_keyword))

        # "request.args.get" -> "get"
        last_attribute = _id.rpartition('.')[-1]
        if definition:
            if isinstance(definition.node, ast.ClassDef):
                self.add_builtin(node)
            elif isinstance(definition.node, ast.FunctionDef):
                self.undecided = False
                return self.process_function(node, definition)
            else:
                raise Exception('Definition was neither FunctionDef or ' +
                                'ClassDef, cannot add the function ')
        elif last_attribute not in NOT_A_BLACKBOX:
            # Mark the call as a blackbox because we don't have the definition
            return self.add_blackbox_call(node)

        return self.add_builtin(node)

    def add_module(self, module, module_or_package_name, local_names, import_alias_mapping, is_init=False, from_from=False, from_fdid=False):
        """
        Returns:
            The ExitNode that gets attached to the CFG of the class.
        """
        module_path = module[1]

        parent_definitions = self.module_definitions_stack[-1]
        # The only place the import_alias_mapping is updated
        parent_definitions.import_alias_mapping.update(import_alias_mapping)
        parent_definitions.import_names = local_names

        new_module_definitions = ModuleDefinitions(local_names, module_or_package_name)
        new_module_definitions.is_init = is_init
        self.module_definitions_stack.append(new_module_definitions)

        # Analyse the file
        self.filenames.append(module_path)
        self.local_modules = get_directory_modules(module_path)
        tree = generate_ast(module_path)

        # Remember, module[0] is None during e.g. "from . import foo", so we must str()
        self.append_node(EntryOrExitNode('Module Entry ' + str(module[0])))
        self.visit(tree)
        exit_node = self.append_node(EntryOrExitNode('Module Exit ' + str(module[0])))

        # Done analysing, pop the module off
        self.module_definitions_stack.pop()
        self.filenames.pop()

        if new_module_definitions.is_init:
            for def_ in new_module_definitions.definitions:
                module_def_alias = handle_aliases_in_init_files(def_.name,
                                                                new_module_definitions.import_alias_mapping)
                parent_def_alias = handle_aliases_in_init_files(def_.name,
                                                                parent_definitions.import_alias_mapping)
                # They should never both be set
                assert not (module_def_alias and parent_def_alias)

                def_name = def_.name
                if parent_def_alias:
                    def_name = parent_def_alias
                if module_def_alias:
                    def_name = module_def_alias

                local_definitions = self.module_definitions_stack[-1]
                if local_definitions != parent_definitions:
                    raise
                if not isinstance(module_or_package_name, str):
                    module_or_package_name = module_or_package_name.name

                if module_or_package_name:
                    if from_from:
                        qualified_name = def_name

                        if from_fdid:
                            alias = handle_fdid_aliases(module_or_package_name, import_alias_mapping)
                            if alias:
                                module_or_package_name = alias
                            parent_definition = ModuleDefinition(parent_definitions,
                                                                 qualified_name,
                                                                 module_or_package_name,
                                                                 self.filenames[-1])
                        else:
                            parent_definition = ModuleDefinition(parent_definitions,
                                                                 qualified_name,
                                                                 None,
                                                                 self.filenames[-1])
                    else:
                        qualified_name = '.'.join([module_or_package_name,
                                                          def_name])
                        parent_definition = ModuleDefinition(parent_definitions,
                                                             qualified_name,
                                                             parent_definitions.module_name,
                                                             self.filenames[-1])
                    parent_definition.node = def_.node
                    parent_definitions.definitions.append(parent_definition)
                else:
                    parent_definition = ModuleDefinition(parent_definitions,
                                                         def_name,
                                                         parent_definitions.module_name,
                                                         self.filenames[-1])
                    parent_definition.node = def_.node
                    parent_definitions.definitions.append(parent_definition)

        return exit_node

    def from_directory_import(self, module, real_names, local_names, import_alias_mapping, skip_init=False):
        """
            Directories don't need to be packages.
        """
        module_path = module[1]

        init_file_location = os.path.join(module_path, '__init__.py')
        init_exists = os.path.isfile(init_file_location)

        if init_exists and not skip_init:
            package_name = os.path.split(module_path)[1]
            return self.add_module((module[0], init_file_location),
                                   package_name,
                                   local_names,
                                   import_alias_mapping,
                                   is_init=True,
                                   from_from=True)
        for real_name in real_names:
            full_name = os.path.join(module_path, real_name)
            if os.path.isdir(full_name):
                new_init_file_location = os.path.join(full_name, '__init__.py')
                if os.path.isfile(new_init_file_location):
                    self.add_module((real_name, new_init_file_location),
                                    real_name,
                                    local_names,
                                    import_alias_mapping,
                                    is_init=True,
                                    from_from=True,
                                    from_fdid=True)
                else:
                    raise Exception("from anything import directory needs an __init__.py file in directory")
            else:
                file_module = (real_name, full_name + '.py')
                self.add_module(file_module, real_name, local_names, import_alias_mapping, from_from=True)

    def import_package(self, module, module_name, local_name, import_alias_mapping):
        module_path = module[1]
        init_file_location = os.path.join(module_path, '__init__.py')
        init_exists = os.path.isfile(init_file_location)
        if init_exists:
            return self.add_module((module[0], init_file_location),
                                   module_name,
                                   local_name,
                                   import_alias_mapping,
                                   is_init=True)
        else:
            raise Exception("import directory needs an __init__.py file")

    def visit_Import(self, node):
        for name in node.names:
            for module in self.local_modules:
                if name.name == module[0]:
                    if os.path.isdir(module[1]):
                        return self.import_package(module,
                                                   name,
                                                   name.asname,
                                                   retrieve_import_alias_mapping(node.names))
                    return self.add_module(module,
                                           name.name,
                                           name.asname,
                                           retrieve_import_alias_mapping(node.names))
            for module in self.project_modules:
                if name.name == module[0]:
                    if os.path.isdir(module[1]):
                        return self.import_package(module,
                                                   name,
                                                   name.asname,
                                                   retrieve_import_alias_mapping(node.names))
                    return self.add_module(module,
                                           name.name,
                                           name.asname,
                                           retrieve_import_alias_mapping(node.names))
        return IgnoredNode()

    def handle_relative_import(self, node):
        """
            from A means node.level == 0
            from . import B means node.level == 1
            from .A means node.level == 1
        """
        no_file = os.path.abspath(os.path.join(self.filenames[-1], os.pardir))
        skip_init = False

        if node.level == 1:
            # Same directory as current file
            if node.module:
                name_with_dir = os.path.join(no_file, node.module.replace('.', '/'))
                if not os.path.isdir(name_with_dir):
                    name_with_dir = name_with_dir + '.py'
            # e.g. from . import X
            else:
                name_with_dir = no_file
                # We do not want to analyse the init file of the current directory
                skip_init = True
        else:
            parent = os.path.abspath(os.path.join(no_file, os.pardir))
            if node.level > 2:
                # Perform extra `cd ..` however many times
                for _ in range(0, node.level - 2):
                    parent = os.path.abspath(os.path.join(parent, os.pardir))
            if node.module:
                name_with_dir = os.path.join(parent, node.module.replace('.', '/'))
                if not os.path.isdir(name_with_dir):
                    name_with_dir = name_with_dir + '.py'
            # e.g. from .. import X
            else:
                name_with_dir = parent

        # Is it a file?
        if name_with_dir.endswith('.py'):
            return self.add_module((node.module, name_with_dir), None,
                                   as_alias_handler(node.names),
                                   retrieve_import_alias_mapping(node.names),
                                   from_from=True)
        return self.from_directory_import((node.module, name_with_dir),
                                          not_as_alias_handler(node.names),
                                          as_alias_handler(node.names),
                                          retrieve_import_alias_mapping(node.names),
                                          skip_init=skip_init)

    def visit_ImportFrom(self, node):
        # Is it relative?
        if node.level > 0:
            return self.handle_relative_import(node)
        else:
            for module in self.local_modules:
                if node.module == module[0]:
                    if os.path.isdir(module[1]):
                        return self.from_directory_import(module,
                                                          not_as_alias_handler(node.names),
                                                          as_alias_handler(node.names))
                    return self.add_module(module, None,
                                           as_alias_handler(node.names),
                                           retrieve_import_alias_mapping(node.names),
                                           from_from=True)
            for module in self.project_modules:
                name = module[0]
                if node.module == name:
                    if os.path.isdir(module[1]):
                        return self.from_directory_import(module,
                                                          not_as_alias_handler(node.names),
                                                          as_alias_handler(node.names),
                                                          retrieve_import_alias_mapping(node.names))
                    return self.add_module(module, None,
                                           as_alias_handler(node.names),
                                           retrieve_import_alias_mapping(node.names),
                                           from_from=True)
        return IgnoredNode()


def interprocedural(node, project_modules, local_modules, filename,
                    module_definitions=None):

    visitor = InterproceduralVisitor(node,
                                     project_modules,
                                     local_modules, filename,
                                     module_definitions)
    return CFG(visitor.nodes, visitor.blackbox_assignments)
