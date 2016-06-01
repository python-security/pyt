"""Draws CFG."""
from graphviz import Digraph
from cfg import AssignmentNode
from itertools import permutations
from subprocess import run

IGNORED_LABEL_NAME_CHARACHTERS = ':'

cfg_styles = {
    'graph': {
        'fontsize': '16',
        'fontcolor': 'black',
        'bgcolor': 'transparent',
        'rankdir': 'TB',
        'splines': 'ortho',
        'margin' : '0.01',
    },
    'nodes': {
        'fontname': 'Gotham',
        'shape': 'box',
        'fontcolor': 'black',
        'color': 'black',
        'style': 'filled',
        'fillcolor': 'transparent',
    },
    'edges': {
        'style': 'filled',
        'color': 'black',
        'arrowhead': 'normal',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'black',
    }
}

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

def draw_cfg(cfg, output_filename = 'output'):
    """Draw CFG and output as pdf."""
    graph = Digraph(format='pdf')
    
    for node in cfg.nodes:
        stripped_label = node.label.replace(IGNORED_LABEL_NAME_CHARACHTERS, '')
        
        if 'Exit' in stripped_label:
            graph.node(stripped_label, 'Exit', shape='none')
        elif 'Entry' in stripped_label:
            graph.node(stripped_label, 'Entry', shape='none')
        else:
            graph.node(stripped_label, stripped_label)
            
        for ingoing_node in node.ingoing:
            graph.edge(ingoing_node.label.replace(IGNORED_LABEL_NAME_CHARACHTERS, ''), stripped_label)

    graph = apply_styles(graph, cfg_styles)
    graph.render(filename = output_filename)


class Node():

    def __init__(self, s, parent, children=None):
        self.s = s
        self.parent = parent
        self.children = children

    def __str__(self):
        return 'Node: ' + str(self.s) + ' Parent: ' + str(self.parent) + ' Children: ' + str(self.children)

    def __hash__(self):
        return hash(str(self.s))


def draw_node(l, graph, node):
    graph.node(str(node.s), str(node.s))
    for child in node.children:
        graph.node(str(child.s), str(child.s))
        if not (str(node.s), str(child.s)) in l:
            graph.edge(str(node.s), str(child.s), )
            l.append((str(node.s), str(child.s)))
        draw_node(l, graph, child)

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

def add_anchor(filename):
    filename += '.dot'
    out = list()
    delimiter = '->'
    with open(filename, 'r') as fd:
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
    with open(filename, 'w') as fd:
        for line in out:
            fd.write(line)

def run_dot(filename):
    filename += '.dot'
    run(['dot', '-Tpdf', filename, '-o', filename.replace('.dot', '.pdf')])

def draw_lattice(cfg, output_filename='output'):
    """Draw CFG and output as pdf."""
    graph = Digraph(format='pdf')

    ll = [s.label for s in cfg.nodes if isinstance(s, AssignmentNode)]
    root = make_lattice(ll,len(ll)-1)
    l = list()
    draw_node(l, graph, root)

    graph = apply_styles(graph, lattice_styles)
    graph.render(filename = output_filename+'.dot')

    add_anchor(output_filename)
    run_dot(output_filename)

def draw_lattices(cfg_list, output_prefix='output'):
    for i, cfg in enumerate(cfg_list):
        draw_lattice(cfg, output_prefix + '_' + str(i))    

def draw_cfgs(cfg_list, output_prefix='output'):
    for i, cfg in enumerate(cfg_list):
        draw_cfg(cfg, output_prefix + '_' + str(i))
