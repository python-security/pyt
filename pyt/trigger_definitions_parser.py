import json
from collections import namedtuple


Definitions = namedtuple(
    'Definitions',
    (
        'sources',
        'sinks'
    )
)


def parse(trigger_word_file):
    """Parse the file for source and sink definitions.

    Returns:
       A definitions tuple with sources and sinks.
    """
    sources = list()
    sinks = list()

    with open(trigger_word_file) as fd:
        trigger_dict = json.load(fd)
        sources = trigger_dict['sources']
        for sink in trigger_dict['sinks']:
            print(f'sink is {sink}')
            sinks.append(sink)

    return Definitions(sources, sinks)
