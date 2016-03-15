from cfg import AssignmentNode

class reaching_definitions_analysis(object):
    def join(self, cfg_node):
        JOIN = set()
        for ingoing in cfg_node.ingoing:
            JOIN |= ingoing.old_constraint
        return JOIN

    def arrow(self, JOIN, _id):
        result = set()
        for cfg_node in JOIN:
            # if there is no intersection _id is not found in the LHS of cfg_node, the node will therefore not be deleted
            if len(_id.intersection(cfg_node.left_hand_side)) == 0: 
                result.add(cfg_node)
        return result
        
    def fixpointmethod(self, cfg_node):
        # Assignment: JOIN(v) arrow(id) join(v)
        if isinstance(cfg_node, AssignmentNode):
            JOIN = self.join(cfg_node)
            arrow_result = self.arrow(JOIN, cfg_node.left_hand_side)
            arrow_result.add(cfg_node)
            cfg_node.new_constraint = arrow_result
            
        else:
            # Default case join(v)
            cfg_node.new_constraint = self.join(cfg_node)
