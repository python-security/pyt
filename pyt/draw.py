from graphviz import Digraph

styles = {
    'graph': {
        'label': 'A Fancy Graph',
        'fontsize': '16',
        'fontcolor': 'black',
        'bgcolor': 'transparent',
        'rankdir': 'TB',
        'splines': 'ortho',
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


def draw_cfg(cfg, title = 'Default Title', output_filename = 'output'):
    graph = Digraph(format='svg')
    
    for x, node in enumerate(cfg.nodes):
        graph.node(node.label)
        for ingoing_node in node.ingoing:
            graph.edge(ingoing_node.label, node.label)

    styles['graph']['label'] = title
    graph = apply_styles(graph, styles)
    graph.render(filename = output_filename)
