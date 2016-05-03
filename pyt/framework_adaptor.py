"""A framework adaptor is a adaptor used to adapt the source code to a specific framework."""
from abc import ABCMeta, abstractmethod


class FrameworkAdaptor(metaclass=ABCMeta):
    """An engine that should be used as base class to specify how to find all sources and sinks."""

    def __init__(self, cfg_list):
        self.cfg_list = cfg_list
        self.run()

    @abstractmethod
    def run(self):
        pass
