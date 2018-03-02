import ast

from .ast_helper import Arguments, generate_ast
from .base_cfg import (
    CALL_IDENTIFIER,
    CFG,
    EntryOrExitNode,
    IgnoredNode,
    Node,
    ReturnNode,
    Visitor
)
from .label_visitor import LabelVisitor
from .right_hand_side_visitor import RHSVisitor


class IntraproceduralVisitor(Visitor):

    def __init__(self, node, filename):
        """Create an empty CFG."""
        self.nodes = list()
        self.undecided = False  # Check if needed in intraprocedural

        self.function_names = list()
        self.filenames = [filename]

        try:
            # FunctionDef ast node
            self.init_function_cfg(node)
        except:  # Error?!
            # Module ast node
            self.init_module_cfg(node)

    def init_module_cfg(self, node):
        entry_node = self.append_node(EntryOrExitNode("Entry module"))

        module_statements = self.visit(node)

        if not module_statements:
            raise Exception('Empty module. It seems that your file is empty,' +
                            ' there is nothing to analyse.')

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

    def init_function_cfg(self, node):

        entry_node = self.append_node(EntryOrExitNode("Entry module"))

        module_statements = self.stmt_star_handler(node.body)
        if isinstance(module_statements, IgnoredNode):
            exit_node = self.append_node(EntryOrExitNode("Exit module"))
            entry_node.connect(exit_node)
            return

        first_node = module_statements.first_statement
        if CALL_IDENTIFIER not in first_node.label:
            entry_node.connect(first_node)

        exit_node = self.append_node(EntryOrExitNode("Exit module"))

        last_nodes = module_statements.last_statements
        exit_node.connect_predecessors(last_nodes)

    def visit_ClassDef(self, node):
        return self.append_node(Node('class ' + node.name, node,
                                     line_number=node.lineno,
                                     path=self.filenames[-1]))

    def visit_FunctionDef(self, node):
        arguments = Arguments(node.args)
        return self.append_node(Node('def ' + node.name + '(' +
                                     ','.join(arguments) + '):',
                                     node,
                                     line_number=node.lineno,
                                     path=self.filenames[-1]))

    def visit_Return(self, node):
        label = LabelVisitor()
        label.visit(node)

        try:
            rhs_visitor = RHSVisitor()
            rhs_visitor.visit(node.value)
        except AttributeError:
            rhs_visitor.result = 'EmptyReturn'

        LHS = 'ret_' + 'MAYBE_FUNCTION_NAME'
        return self.append_node(ReturnNode(LHS + ' = ' + label.result,
                                           LHS,
                                           node,
                                           rhs_visitor.result,
                                           line_number=node.lineno,
                                           path=self.filenames[-1]))

    def visit_Yield(self, node):
        label = LabelVisitor()
        label.visit(node)

        try:
            rhs_visitor = RHSVisitor()
            rhs_visitor.visit(node.value)
        except AttributeError:
            rhs_visitor.result = 'EmptyYield'

        LHS = 'yield_' + 'MAYBE_FUNCTION_NAME'
        return self.append_node(ReturnNode(LHS + ' = ' + label.result,
                                           LHS,
                                           node,
                                           rhs_visitor.result,
                                           line_number=node.lineno,
                                           path=self.filenames[-1]))

    def visit_Call(self, node):
        return self.add_builtin(node)

    def visit_Import(self, node):
        names = [n.name for n in node.names]
        return self.append_node(Node('Import ' + ', '.join(names), node,
                                     line_number=node.lineno,
                                     path=self.filenames[-1]))

    def visit_ImportFrom(self, node):
        names = [a.name for a in node.names]
        try:
            from_import = 'from ' + node.module + ' '
        except TypeError:
            from_import = ''
        return self.append_node(Node(from_import + 'import ' +
                                     ', '.join(names),
                                     node,
                                     line_number=node.lineno,
                                     path=self.filenames[-1]))


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
