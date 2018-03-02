import ast

from .base_cfg import AssignmentNode
from .constraint_table import constraint_table
from .lattice import Lattice
from .reaching_definitions import ReachingDefinitionsAnalysis
from .vars_visitor import VarsVisitor


def get_vars(node):
    vv = VarsVisitor()
    if isinstance(node.ast_node, ast.While)\
       or isinstance(node.ast_node, ast.If):
        vv.visit(node.ast_node.test)
    elif isinstance(node.ast_node, ast.FunctionDef) or\
         isinstance(node.ast_node, ast.ClassDef):
        return list()
    else:
        try:
            vv.visit(node.ast_node)
        except AttributeError:  # If no ast_node
            vv.result = list()

    vv.result = set(vv.result)

    # Filter out lvars:
    for var in vv.result:
        try:  # if assignment node
            # print('r', node.right_hand_side_variables)
            # if var not in node.left_hand_side:
            if var in node.right_hand_side_variables:
                yield var
        except AttributeError:
            yield var


def get_constraint_nodes(node, lattice):
    for n in lattice.get_elements(constraint_table[node]):
        if n is not node:
            yield n


def build_use_def_chain(cfg_nodes):
    use_def = dict()
    lattice = Lattice(cfg_nodes, ReachingDefinitionsAnalysis)

    for node in cfg_nodes:
        definitions = list()
        for cnode in get_constraint_nodes(node, lattice):
            for var in get_vars(node):
                if var in cnode.left_hand_side:
                    definitions.append((var, cnode))
        use_def[node] = definitions

    return use_def


def varse(node):
    vv = VarsVisitor()
    if isinstance(node.ast_node, ast.FunctionDef) or\
       isinstance(node.ast_node, ast.ClassDef):
        return list()
    elif isinstance(node.ast_node, ast.While)\
            or isinstance(node.ast_node, ast.If):
        vv.visit(node.ast_node.test)
    else:
        try:
            vv.visit(node.ast_node)
        except AttributeError:
            return list()

    if isinstance(node, AssignmentNode):
        result = list()
        for var in vv.result:
            if var not in node.left_hand_side:
                result.append(var)
        return result
    else:
        return vv.result


def build_def_use_chain(cfg_nodes):
    def_use = dict()
    lattice = Lattice(cfg_nodes, ReachingDefinitionsAnalysis)

    for node in cfg_nodes:
        if isinstance(node, AssignmentNode):
            def_use[node] = list()

    for node in cfg_nodes:
        for var in varse(node):
            for cnode in get_constraint_nodes(node, lattice):
                if var in cnode.left_hand_side:
                    def_use[cnode].append(node)
    return def_use
