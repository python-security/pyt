import ast
from collections import namedtuple

from base_cfg import Visitor, Node, CFG, EntryExitNode
from label_visitor import LabelVisitor
from right_hand_side_visitor import RHSVisitor
from ast_helper import generate_ast, get_call_names_as_string, Arguments


class IntraproceduralVisitor(Visitor):

    def __init__(self, node, filename):
        """Create an empty CFG."""
        self.nodes = list()
        self.undecided = False  # Check if needed in intraprocedural

        self.function_names = list()  # Probably not necessary check https://github.com/SW10IoT/pyt/issues/23
        self.function_return_stack = list()  # Same as above

        self.filenames = [filename]

        try:
            # FunctionDef ast node
            self.init_function_cfg(node)
        except:  # Error?!
            # Module ast node
            self.init_module_cfg(node)

    def init_module_cfg(self, node):
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

    def init_function_cfg(self, node):
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

    def visit_ClassDef(self, node):
        # Something here? y or n ?
        pass

    def visit_FunctionDef(self, node):
        # Something here? y or n ?
        pass

    def visit_Return(self, node):
        # Something here? y or n ?
        pass

    def visit_Call(self, node):
        return self.add_builtin(node)

    # Import and ImportFrom?


class FunctionDefVisitor(ast.NodeVisitor):
    def __init__(self):
        self.result = list()

    def visit_FunctionDef(self, node):
        self.result.append(node)
    #def visit_ClassDef(self, node):
     #   self.result.append(node)


def intraprocedural(project_modules, cfg_list):
    functions = list()
    dup = list()
    for module in project_modules:
        t = generate_ast(module[1])
        iv = IntraproceduralVisitor(t, filename=module[1])
        cfg_list.append(CFG(iv.nodes))
        dup.append(t)
        fdv = FunctionDefVisitor()
        fdv.visit(t)
        dup.extend(fdv.result)
        functions.extend([(f, module[1]) for f in fdv.result])

    for f in functions:
        iv = IntraproceduralVisitor(f[0], filename=f[1])
        cfg_list.append(CFG(iv.nodes))

    s = set()
    for d in dup:
        if d in s:
            raise Exception('Duplicates in the functions definitions list.')
        else:
            s.add(d)
