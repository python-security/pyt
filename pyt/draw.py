from graphviz import Digraph

def draw_cfg(cfg, output_filename = 'output'):
    graph = Digraph(format='svg')
    
    for x, node in enumerate(cfg.nodes):
        graph.node(node.label)
        for ingoing_node in node.ingoing:
            graph.edge(ingoing_node.label, node.label)

    graph.render(filename = output_filename)
