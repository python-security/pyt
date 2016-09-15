import ast
from collections import namedtuple
import logging

from label_visitor import LabelVisitor
from right_hand_side_visitor import RHSVisitor
from module_definitions import ModuleDefinition, ModuleDefinitions,\
    LocalModuleDefinition
from project_handler import get_directory_modules
from ast_helper import generate_ast, get_call_names_as_string, Arguments
from base_cfg import EntryExitNode, Node

CALL_IDENTIFIER = '¤'
SavedVariable = namedtuple('SavedVariable', 'LHS RHS')


class InterproceduralVisitor(Visitor):
    def __init__(self, node, project_modules, local_modules, filename, module_definitions=None):
        """Create an empty CFG."""
        self.nodes = list()
        self.function_index = 0
        self.undecided = False
        self.project_modules = project_modules
        self.local_modules = local_modules
        self.function_names = list()
        self.function_return_stack = list()
        self.module_definitions_stack = list()
        self.filenames = [filename]

        if module_definitions:
            self.init_function_cfg(node, module_definitions)
        else:
            self.init_cfg(node)


    def init_cfg(self, node):
        self.module_definitions_stack.append(ModuleDefinitions())
        
        entry_node = self.append_node(EntryExitNode("Entry module"))
                
        module_statements = self.visit(node)

        if not module_statements:
            raise Exception('Empty module. It seems that your file is empty, there is nothing to analyse.')
        
        if not isinstance(module_statements, IgnoredNode):
            first_node = module_statements.first_statement

            if CALL_IDENTIFIER not in first_node.label:
                entry_node.connect(first_node)

            exit_node = self.append_node(EntryExitNode("Exit module"))

            last_nodes = module_statements.last_statements
            exit_node.connect_predecessors(last_nodes)
        else:
            exit_node = self.append_node(EntryExitNode("Exit module"))    
            entry_node.connect(exit_node)

    def init_function_cfg(self, node, module_definitions):
        self.module_definitions_stack.append(module_definitions)
        
        self.function_names.append(node.name)
        self.function_return_stack.append(node.name)
        
        entry_node = self.append_node(EntryExitNode("Entry module"))
                
        module_statements = self.stmt_star_handler(node.body)

        first_node = module_statements.first_statement
        
        if CALL_IDENTIFIER not in first_node.label:
            entry_node.connect(first_node)

        exit_node = self.append_node(EntryExitNode("Exit module"))
        
        last_nodes = module_statements.last_statements
        exit_node.connect_predecessors(last_nodes)

    def visit_ClassDef(self, node):
        logger.debug(node.name)
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
        logger.debug(node.name)
        self.add_to_definitions(node)
        
        return IgnoredNode()

    def add_to_definitions(self, node):
        local_definitions = self.module_definitions_stack[-1]
        parent_definitions = self.get_parent_definitions()

        if parent_definitions:
            parent_qualified_name = '.'.join(parent_definitions.classes + [node.name])
            parent_definition = ModuleDefinition(parent_definitions, parent_qualified_name, local_definitions.module_name, self.filenames[-1])
            parent_definition.node = node
            parent_definitions.append(parent_definition)

        local_qualified_name = '.'.join(local_definitions.classes + [node.name])
        local_definition = LocalModuleDefinition(local_definitions, local_qualified_name, None, self.filenames[-1])
        local_definition.node = node
        local_definitions.append(local_definition)

        self.function_names.append(node.name)
    
    def return_connection_handler(self, nodes, exit_node):
        """Connect all return statements to the Exit node."""
        for function_body_node in nodes:
            if isinstance(function_body_node, ConnectToExitNode):
                if not exit_node in function_body_node.outgoing:
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
        return self.append_node(ReturnNode(LHS + ' = ' + label.result, LHS, rhs_visitor.result, node, line_number = node.lineno, path=self.filenames[-1]))
        

    def save_local_scope(self, line_number):
        """Save the local scope before entering a function call."""
        saved_variables = list()
        for assignment in [node for node in self.nodes if type(node) == AssignmentNode]:
            if isinstance(assignment, RestoreNode):
                continue
           
        # above can be optimized with the assignments dict
            save_name = 'save_' + str(self.function_index) + '_' + assignment.left_hand_side
            previous_node = self.nodes[-1]
            saved_scope_node = self.append_node(RestoreNode(save_name + ' = ' + assignment.left_hand_side, save_name, [assignment.left_hand_side], line_number=line_number, path=self.filenames[-1]))
            
            saved_variables.append(SavedVariable(LHS = save_name, RHS = assignment.left_hand_side))
            previous_node.connect(saved_scope_node)
        return saved_variables

    def save_actual_parameters_in_temp(self, args, arguments, line_number):
        """Save the actual parameters of a function call."""
        parameters = dict()
        for i, parameter in enumerate(args):
            temp_name = 'temp_' + str(self.function_index) + '_' + arguments[i]

            label_visitor = LabelVisitor()
            label_visitor.visit(parameter)        
            n = RestoreNode(temp_name + ' = ' + label_visitor.result, temp_name, [label_visitor.result], line_number=line_number, path=self.filenames[-1])
            
            self.nodes[-1].connect(n)
            self.nodes.append(n)

            parameters[label_visitor.result] = arguments[i]
        return parameters

    def create_local_scope_from_actual_parameters(self, args, arguments, line_number):
        """Create the local scope before entering the body of a function call."""
        parameters = dict()
        for i, parameter in enumerate(args):
            temp_name = 'temp_' + str(self.function_index) + '_' + arguments[i]                
            local_name = arguments[i]
            previous_node = self.nodes[-1]
            local_scope_node = self.append_node(RestoreNode(local_name + ' = ' + temp_name, local_name, [temp_name], line_number=line_number, path=self.filenames[-1]))
            previous_node.connect(local_scope_node)

    def restore_saved_local_scope(self, saved_variables, parameters, line_number):
        """Restore the previously saved variables to their original values.

        Args:
           saved_variables(list[SavedVariable]).
        """
        restore_nodes = list()
        for var in saved_variables:
            if var.RHS in parameters:
                restore_nodes.append(RestoreNode(var.RHS + ' = ' + parameters[var.RHS], var.RHS, [var.LHS], line_number=line_number, path=self.filenames[-1]))
            else:
                restore_nodes.append(RestoreNode(var.RHS + ' = ' + var.LHS, var.RHS, [var.LHS], line_number=line_number, path=self.filenames[-1]))

        for n, successor in zip(restore_nodes, restore_nodes[1:]):
            n.connect(successor)

        if restore_nodes:
            self.nodes[-1].connect(restore_nodes[0])
            self.nodes.extend(restore_nodes)

        return restore_nodes

    def return_handler(self, node, function_nodes, restore_nodes):
        """Handle the return from a function during a function call."""
        call_node = None
        for n in function_nodes:
            if isinstance(n, ConnectToExitNode):
                LHS = CALL_IDENTIFIER + 'call_' + str(self.function_index)
                previous_node = self.nodes[-1]
                if not call_node:
                    RHS = 'ret_' + get_call_names_as_string(node.func)
                    call_node = self.append_node(RestoreNode(LHS + ' = ' + RHS, LHS, [RHS], line_number=node.lineno, path=self.filenames[-1]))
                    previous_node.connect(call_node)
                    
            else:
                # lave rigtig kobling
                pass

    def add_function(self, call_node, definition):
        try:
            self.function_index += 1
            def_node = definition.node
            saved_variables = self.save_local_scope(def_node.lineno)

            parameters = self.save_actual_parameters_in_temp(call_node.args, Arguments(def_node.args), call_node.lineno)

            self.filenames.append(definition.path)
            self.create_local_scope_from_actual_parameters(call_node.args, Arguments(def_node.args), def_node.lineno)
            function_nodes = self.get_function_nodes(definition)
            self.filenames.pop() # Maybe move after restore nodes
            restore_nodes = self.restore_saved_local_scope(saved_variables, parameters, def_node.lineno)
            self.return_handler(call_node, function_nodes, restore_nodes)
            self.function_return_stack.pop()

        except IndexError:
            error_call = get_call_names_as_string(call_node.func)
            print('Error: Possible nameclash in "{}". Call omitted!\n'.format(error_call))


        return self.nodes[-1]

    def get_function_nodes(self, definition):
        length = len(self.nodes)
        previous_node = self.nodes[-1]
        entry_node = self.append_node(EntryExitNode("Entry " + definition.name))
        previous_node.connect(entry_node)
        function_body_connect_statements = self.stmt_star_handler(definition.node.body)
        
        entry_node.connect(function_body_connect_statements.first_statement)

        exit_node = self.append_node(EntryExitNode("Exit " + definition.name))
        exit_node.connect_predecessors(function_body_connect_statements.last_statements)

        self.return_connection_handler(self.nodes[length:], exit_node)

        return self.nodes[length:]

    def visit_Call(self, node):
        _id = get_call_names_as_string(node.func)
        self.function_return_stack.append(_id)
        logging.debug(_id)

        ast_node = None

        local_definitions = self.module_definitions_stack[-1]
        definition = local_definitions.get_definition(_id)
    
        if definition:
            if isinstance(definition.node, ast.ClassDef):
                init = local_definitions.get_definition(_id + '.__init__')
                self.add_builtin(node)
            elif isinstance(definition.node, ast.FunctionDef):
                self.undecided = False
                return self.add_function(node, definition)
            else:
                raise Exception('Definition was neither FunctionDef or ClassDef, cannot add the function ')
        return self.add_builtin(node)

    def add_class(self, call_node, def_node):
        label_visitor = LabelVisitor()
        label_visitor.visit(call_node)

        previous_node = self.nodes[-1]

        entry_node = self.append_node(EntryExitNode("Entry " + def_node.name))

        previous_node.connect(entry_node)

        function_body_connect_statements = self.stmt_star_handler(def_node.body)
        
        entry_node.connect(function_body_connect_statements.first_statement)

        exit_node = self.append_node(EntryExitNode("Exit " + def_node.name))
        exit_node.connect_predecessors(function_body_connect_statements.last_statements)

        return Node(label_visitor.result, call_node, line_number=call_node.lineno, path=self.filenames[-1])

    def add_module(self, module, module_name, local_names):
        module_path = module[1]
        self.filenames.append(module_path)
        self.local_modules = get_directory_modules(module_path)
        tree = generate_ast(module_path)

        parent_definitions = self.module_definitions_stack[-1]
        parent_definitions.import_names = local_names

        module_definitions = ModuleDefinitions(local_names, module_name)
        self.module_definitions_stack.append(module_definitions)

        self.append_node(EntryExitNode('Entry ' + module[0]))
        self.visit(tree)
        exit_node = self.append_node(EntryExitNode('Exit ' + module[0]))

        self.module_definitions_stack.pop()
        self.filenames.pop()

        return exit_node

    def visit_Import(self, node):
        for name in node.names:
            for module in self.local_modules:
                if name.name == module[0]:
                    return self.add_module(module, name.name, name.asname)
            for module in self.project_modules:
                if name.name == module[0]:
                    return self.add_module(module, name.name, name.asname)
        return IgnoredNode()

    def alias_handler(self, alias_list):
        l = list()
        for alias in alias_list:
            if alias.asname:
                l.append(alias.asname)
            else:
                l.append(alias.name)
        return l

    def visit_ImportFrom(self, node):
        for module in self.local_modules:
            if node.module == module[0]:
                return self.add_module(module, None, self.alias_handler(node.names))
        for module in self.project_modules:
            if node.module == module[0]:
                    return self.add_module(module, None, self.alias_handler(node.names))
        return IgnoredNode()
