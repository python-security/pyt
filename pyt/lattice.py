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

lattice_styles = {
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

def draw_node(l, graph, node):
    graph.node(str(node.s), str(node.s))
    for child in node.children:
        graph.node(str(child.s), str(child.s))
        if not (str(node.s), str(child.s)) in l:
            graph.edge(str(node.s), str(child.s), )
            l.append((str(node.s), str(child.s)))
        draw_node(l, graph, child)

def draw_lattice(node, output_filename = 'output.dot'):
    """Draw CFG and output as pdf."""
    graph = Digraph(format='pdf')

    l = list()
    draw_node(l, graph, node)

    graph = apply_styles(graph, styles)
    graph.render(filename = output_filename)

def make_lattice(s, length):
    p = Node(s, None)
    p.children = get_children(p, s, length)
    return p

def get_children(p, s, length):
    children = set()
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
            children.add(n)
    return children

def add_anchor():
    out = list()
    delimiter = '->'
    with open('output.dot', 'r') as fd:
        for line in fd:
            if delimiter in line:
                s = line.split(delimiter)
                ss = s[0][:-1]
                s[0] = ss + ':s '
                ss = s[1][:-1]
                s[1] = ss + ':n\n'
                s.insert(1, delimiter)
                out.append(''.join(s))
            else:
                out.append(line)
    with open('output.dot', 'w') as fd:
        for line in out:
            fd.write(line)

if __name__ == '__main__':
    s = {1,2,3,4}
    p = make_lattice(s, 3)
    draw_lattice(p)
    add_anchor()
