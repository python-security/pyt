"""Draws CFG."""
from graphviz import Digraph

IGNORED_LABEL_NAME_CHARACHTERS = ':'

styles = {
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
        
        print(stripped_label)
        if 'Exit' in stripped_label:
            graph.node(stripped_label, 'Exit', shape='none')
        elif 'Entry' in stripped_label:
            graph.node(stripped_label, 'Entry', shape='none')
        else:
            graph.node(stripped_label, stripped_label)
            
        for ingoing_node in node.ingoing:
            graph.edge(ingoing_node.label.replace(IGNORED_LABEL_NAME_CHARACHTERS, ''), stripped_label)

    graph = apply_styles(graph, styles)
    graph.render(filename = output_filename)

def draw_cfgs(cfg_list, output_prefix='output'):
    for i, cfg in enumerate(cfg_list):
        draw_cfg(cfg, output_prefix + '_' + str(i))
