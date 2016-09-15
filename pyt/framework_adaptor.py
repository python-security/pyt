"""A framework adaptor is a adaptor used to adapt the source code to a specific framework."""
from abc import ABCMeta, abstractmethod
from base_cfg import AssignmentNode

class FrameworkAdaptor(metaclass=ABCMeta):
    """An engine that should be used as base class to specify how to find all sources and sinks."""

    def __init__(self, cfg_list, project_modules, local_modules):
        self.cfg_list = cfg_list
        self.project_modules = project_modules
        self.local_modules = local_modules
        self.run()

    @abstractmethod
    def run(self):
        pass

class TaintedNode(AssignmentNode):
    pass
