"""This module contains classes for generating a Control Flow Graph
of a python program.

The class Visitor is the main entry point to this module.
It uses the visitor pattern implemented by the ast module from the
standard library.
"""

import ast
from collections import namedtuple
import logging

from label_visitor import LabelVisitor
from right_hand_side_visitor import RHSVisitor
from module_definitions import ModuleDefinition, ModuleDefinitions,\
    LocalModuleDefinition
from project_handler import get_directory_modules
from ast_helper import generate_ast, get_call_names_as_string, Arguments


CALL_IDENTIFIER = '¤'

SavedVariable = namedtuple('SavedVariable', 'LHS RHS')


class Visitor(ast.NodeVisitor):
    """A Control Flow Graph containing a list of nodes."""
    
    def __init__(self, node, project_modules, local_modules, filename, module_definitions=None, intraprocedural=False):
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
        self.intraprocedural = intraprocedural

        if intraprocedural:
            self.init_intra_function_cfg(node)
        elif module_definitions:
            self.init_function_cfg(node, module_definitions)
        else:
            self.init_cfg(node)

    def init_intra_function_cfg(self, node):
        self.module_definitions_stack.append(ModuleDefinitions())        
        self.function_names.append(node.name)
        self.function_return_stack.append(node.name)
        
        entry_node = self.append_node(EntryExitNode("Entry module"))

        module_statements = self.stmt_star_handler(node.body)
        if isinstance(module_statements, IgnoredNode):
            exit_node = self.append_node(EntryExitNode("Exit module"))
            entry_node.connect(exit_node)
            return

        first_node = module_statements.first_statement
        if CALL_IDENTIFIER not in first_node.label:
            entry_node.connect(first_node)

        exit_node = self.append_node(EntryExitNode("Exit module"))
        
        last_nodes = module_statements.last_statements
        exit_node.connect_predecessors(last_nodes)

