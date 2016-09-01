"""Thos module contains a base class for the analysis component used in PyT."""
from abc import abstractmethod, ABCMeta


class AnalysisBase(metaclass=ABCMeta):
    """Base class for fixed point analyses."""

    annotated_cfg_nodes = dict()

    def __init__(self, cfg, visitor):
        """Annotate visitor if not None and save visitor."""
        if visitor:
            self.annotate_cfg(cfg, visitor)
        self.visitor = visitor
        self.cfg = cfg

    def annotate_cfg(self, cfg, visitor):
        """Add the visitor to the cfg nodes."""
        for node in cfg.nodes:
            if node.ast_node:
                _visitor = visitor()
                _visitor.visit(node.ast_node)
                self.annotated_cfg_nodes[node] = _visitor.result

    @staticmethod
    @abstractmethod
    def get_lattice_elements(self, cfg_nodes):
        pass

    def dep(self, q_1): # Useless to have this as a function atm
        """Represents the dep mapping from Schwartzbach."""
        for node in self.cfg.nodes:
            yield node

