import json
from collections import namedtuple


Definitions = namedtuple(
    'Definitions',
    (
        'sources',
        'sinks'
    )
)

Source = namedtuple('Source', ('trigger_word'))


class Sink:
    def __init__(
        self, trigger, *,
        unlisted_args_propagate=True, unlisted_kwargs_propagate=True,
        arg_list=None, kwarg_list=None,
        sanitisers=None
    ):
        self._trigger = trigger
        self.sanitisers = sanitisers or []
        self.arg_list_propagates = not unlisted_args_propagate
        self.kwarg_list_propagates = not unlisted_kwargs_propagate

        if trigger[-1] != '(':
            if self.arg_list_propagates or self.kwarg_list_propagates or arg_list or kwarg_list:
                raise ValueError("Propagation options specified, but trigger word isn't a function call")

        self.arg_list = set(arg_list or ())
        self.kwarg_list = set(kwarg_list or ())

    def arg_propagates(self, index):
        in_list = index in self.arg_list
        return self.arg_list_propagates == in_list

    def kwarg_propagates(self, keyword):
        in_list = keyword in self.kwarg_list
        return self.kwarg_list_propagates == in_list

    @property
    def all_arguments_propagate_taint(self):
        if self.arg_list or self.kwarg_list:
            return False
        return True

    @property
    def call(self):
        if self._trigger[-1] == '(':
            return self._trigger[:-1]
        return None

    @property
    def trigger_word(self):
        return self._trigger

    @classmethod
    def from_json(cls, key, data):
        return cls(trigger=key, **data)


def parse(trigger_word_file):
    """Parse the file for source and sink definitions.

    Returns:
       A definitions tuple with sources and sinks.
    """
    with open(trigger_word_file) as fd:
        triggers_dict = json.load(fd)
    sources = [Source(s) for s in triggers_dict['sources']]
    sinks = [
        Sink.from_json(trigger, data)
        for trigger, data in triggers_dict['sinks'].items()
    ]
    return Definitions(sources, sinks)
