"""This module implements the fixed point algorithm."""
from .constraint_table import constraint_table


class FixedPointAnalysis():
    """Run the fix point analysis."""

    def __init__(self, cfg, analysis):
        """Fixed point analysis.

        Analysis must be a dataflow analysis containing a 'fixpointmethod'
        method that analyses one CFG node."""
        self.analysis = analysis(cfg)
        self.cfg = cfg

    def fixpoint_runner(self):
        """Work list algorithm that runs the fixpoint algorithm."""
        q = self.cfg.nodes

        while q != []:
            x_i = constraint_table[q[0]]  # x_i = q[0].old_constraint
            self.analysis.fixpointmethod(q[0])  # y = F_i(x_1, ..., x_n);
            y = constraint_table[q[0]]  # y = q[0].new_constraint

            if not self.analysis.equal(y, x_i):
                for node in self.analysis.dep(q[0]):  # for (v in dep(v_i))
                    q.append(node)  # q.append(v):
                constraint_table[q[0]] = y  # q[0].old_constraint = q[0].new_constraint # x_i = y
            q = q[1:]  # q = q.tail() # The list minus the head


def analyse(cfg_list, *, analysis_type):
    """Analyse a list of control flow graphs with a given analysis type."""
    for cfg in cfg_list:
        analysis = FixedPointAnalysis(cfg, analysis_type)
        analysis.fixpoint_runner()
