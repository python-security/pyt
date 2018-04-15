try:
    value = None
except ImportError:
    value = 1

"""
        if node.orelse:
            orelse_last_nodes = self.handle_or_else(node.orelse, try_node)
            body.last_statements.extend(orelse_last_nodes)
        else:
            body.last_statements.append(try_node) # if there is no orelse, test needs an edge to the next_node
        if node.finalbody:
            finalbody_last_nodes = self.handle_or_else(node.finalbody, try_node)
            body.last_statements.extend(finalbody_last_nodes)
        else:
            body.last_statements.append(try_node) # if there is no orelse, test needs an edge to the next_node
"""
