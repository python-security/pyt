"""This module contains a base class for the analysis component used in PyT."""
from abc import ABCMeta, abstractmethod


class AnalysisBase(metaclass=ABCMeta):
    """Base class for fixed point analyses."""

    annotated_cfg_nodes = dict()

    def __init__(self, cfg, visitor):
        """Annotate visitor if not None and save visitor."""
        if visitor:
            self.annotate_cfg(cfg, visitor)
        self.visitor = visitor
        self.cfg = cfg
        self.build_lattice(cfg)

    def annotate_cfg(self, cfg, visitor):
        """Add the visitor to the cfg nodes."""
        for node in cfg.nodes:
            if node.ast_node:
                _visitor = visitor()
                _visitor.visit(node.ast_node)
                self.annotated_cfg_nodes[node] = _visitor.result

    @staticmethod
    @abstractmethod
    def get_lattice_elements(cfg_nodes):
        pass

    @abstractmethod
    def equal(self, value, other):
        """Define the equality for two constraint sets
        that are defined by bitvectors."""
        pass

    @abstractmethod
    def build_lattice(self, cfg):
        pass

    @abstractmethod
    def dep(self, q_1):
        """Represents the dep mapping from Schwartzbach."""
        pass
