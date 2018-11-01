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
        unlisted_args_propagate=True,
        arg_dict=None,
        sanitisers=None,
    ):
        self._trigger = trigger
        self.sanitisers = sanitisers or []
        self.arg_list_propagates = not unlisted_args_propagate

        if trigger[-1] != '(':
            if self.arg_list_propagates or arg_dict:
                raise ValueError("Propagation options specified, but trigger word isn't a function call")

        arg_dict = {} if arg_dict is None else arg_dict
        self.arg_position_to_kwarg = {
            position: name for name, position in arg_dict.items() if position is not None
        }
        self.kwarg_list = set(arg_dict.keys())

    def arg_propagates(self, index):
        kwarg = self.get_kwarg_from_position(index)
        return self.kwarg_propagates(kwarg)

    def kwarg_propagates(self, keyword):
        in_list = keyword in self.kwarg_list
        return self.arg_list_propagates == in_list

    def get_kwarg_from_position(self, index):
        return self.arg_position_to_kwarg.get(index)

    @property
    def all_arguments_propagate_taint(self):
        if self.kwarg_list:
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
