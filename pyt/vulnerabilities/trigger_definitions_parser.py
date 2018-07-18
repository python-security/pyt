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
        sanitisers=None
    ):
        self._trigger = trigger
        self.sanitisers = sanitisers or []

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
