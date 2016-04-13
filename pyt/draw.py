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
    graph = Digraph(format='pdf')
    
    for node in cfg.nodes:
        if node.label == 'Exit node':
            graph.node(node.label, 'Exit', shape='none')
        elif node.label == 'Entry node':
            graph.node(node.label, 'Entry', shape='none')
        else:
            graph.node(node.label.strip(IGNORED_LABEL_NAME_CHARACHTERS), node.label)
        for ingoing_node in node.ingoing:
            graph.edge(ingoing_node.label, node.label)

    graph = apply_styles(graph, styles)
    graph.render(filename = output_filename)
