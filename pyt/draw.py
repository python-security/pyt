from graphviz import Digraph

styles = {
    'graph': {
        'label': 'A Fancy Graph',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'hexagon',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
    },
    'edges': {
        'style': 'dashed',
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
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
    graph = Digraph(format='svg')
    
    for x, node in enumerate(cfg.nodes):
        graph.node(node.label)
        for ingoing_node in node.ingoing:
            graph.edge(ingoing_node.label, node.label)

    graph = apply_styles(graph, styles)
    graph.render(filename = output_filename)
