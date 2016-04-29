import os
from collections import namedtuple

from cfg import CFG, generate_ast, Node
from vulnerability_log import Vulnerability, VulnerabilityLog


class Adaptor(object):
    """An engine that should be used as base class to specify how to find all sources and sinks."""

    def __init__(self, cfg_list):
        self.cfg_list = cfg_list
        self.run()

    def run(self):
        raise NotImplementedError('Should be implemented.')
