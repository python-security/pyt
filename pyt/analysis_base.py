class AnalysisBase(object):
    '''Base class for fixed point analyses.'''

    annotated_cfg_nodes = dict()
    
    def __init__(self, cfg, visitor):
        if visitor:
            self.annotate_cfg(cfg, visitor)
        self.visitor = visitor

    def annotate_cfg(self, cfg, visitor):
        for node in cfg.nodes:
            if node.ast_node:
                _visitor = visitor()
                _visitor.visit(node.ast_node)
                self.annotated_cfg_nodes[node] = _visitor.result


        
    
