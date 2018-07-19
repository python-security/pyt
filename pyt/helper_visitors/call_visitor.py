import ast
import re
from collections import defaultdict, namedtuple
from itertools import count

from ..core.ast_helper import get_call_names_as_string
from .right_hand_side_visitor import RHSVisitor


class CallVisitorResults(
    namedtuple(
        "CallVisitorResults",
        ("args", "kwargs", "unknown_args", "unknown_kwargs")
    )
):
    __slots__ = ()

    def all_results(self):
        for x in self.args:
            yield from x
        for x in self.kwargs.values():
            yield from x
        yield from self.unknown_args
        yield from self.unknown_kwargs


class CallVisitor(ast.NodeVisitor):
    def __init__(self, trigger_str):
        self.unknown_arg_visitor = RHSVisitor()
        self.unknown_kwarg_visitor = RHSVisitor()
        self.argument_visitors = defaultdict(lambda: RHSVisitor())
        self._trigger_str = trigger_str

    def visit_Call(self, call_node):
        func_name = get_call_names_as_string(call_node.func)
        trigger_re = r"(^|\.){}$".format(re.escape(self._trigger_str))
        if re.search(trigger_re, func_name):
            seen_starred = False
            for index, arg in enumerate(call_node.args):
                if isinstance(arg, ast.Starred):
                    seen_starred = True
                if seen_starred:
                    self.unknown_arg_visitor.visit(arg)
                else:
                    self.argument_visitors[index].visit(arg)

            for keyword in call_node.keywords:
                if keyword.arg is None:
                    self.unknown_kwarg_visitor.visit(keyword.value)
                else:
                    self.argument_visitors[keyword.arg].visit(keyword.value)
        self.generic_visit(call_node)

    @classmethod
    def get_call_visit_results(cls, trigger_str, node):
        visitor = cls(trigger_str)
        visitor.visit(node)

        arg_results = []
        for i in count():
            try:
                arg_results.append(set(visitor.argument_visitors.pop(i).result))
            except KeyError:
                break

        return CallVisitorResults(
            arg_results,
            {k: set(v.result) for k, v in visitor.argument_visitors.items()},
            set(visitor.unknown_arg_visitor.result),
            set(visitor.unknown_kwarg_visitor.result),
        )
