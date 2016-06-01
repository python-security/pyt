from itertools import permutations


class Node():

    def __init__(self, s, parent, children=None):
        self.s = s
        self.parent = parent
        self.children = children

    def __str__(self):
        return 'Node: ' + str(self.s) + ' Parent: ' + str(self.parent) + ' Children: ' + str(self.children)

    def __hash__(self):
        return hash(str(self.s))

            
from graphviz import Digraph

IGNORED_LABEL_NAME_CHARACHTERS = ':'

styles = {
    'graph': {
        'fontsize': '16',
        'fontcolor': 'black',
        'bgcolor': 'transparent',
        'rankdir': 'TB',
        'splines': 'line',
        'margin' : '0.01',
        'ranksep': '1',
    },
    'nodes': {
        'fontname': 'Gotham',
        'shape': 'none',
        'fontcolor': 'black',
        'color': 'black',
        'style': 'filled',
        'fillcolor': 'transparent',
    },
    'edges': {
        'style': 'filled',
        'color': 'black',
        'arrowhead': 'none',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'black',
    }
}

def apply_styles(graph, styles):
    """Apply styles to graph."""
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph

def draw_node(graph, node):
    graph.node(str(node.s), str(node.s))
    for child in node.children:
        graph.node(str(child.s), str(child.s))
        graph.edge(str(node.s), str(child.s))
        draw_node(graph, child)

def draw_lattice(node, output_filename = 'output'):
    """Draw CFG and output as pdf."""
    graph = Digraph(format='pdf')

    draw_node(graph, node)
    
    graph = apply_styles(graph, styles)
    graph.render(filename = output_filename)

def make_lattice(s, length):
    p = Node(s, None)
    p.children = get_children(p, s, length)
    return p

def get_children(p, s, length):
    children = list()
    if length < 0:
        return children
    for subset in permutations(s, length):
        setsubset = set(subset)
        append = True
        for node in children:
            if setsubset == node.s:
                append = False
                break
        n = Node(setsubset, p)
        n.children = get_children(n, setsubset, length-1)
        if append:
            children.append(n)
    return children

if __name__ == '__main__':
    s = {1,2,3,4}
    p = make_lattice(s, 3)
    draw_lattice(p)
