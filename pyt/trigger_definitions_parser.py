import os
from collections import namedtuple


SANITISER_SEPARATOR = '->'
SOURCES_KEYWORD = 'sources:'
SINKS_KEYWORD = 'sinks:'

Definitions = namedtuple('Definitions', 'sources sinks')
default_trigger_word_file = os.path.join(os.path.dirname(__file__),
                                         'trigger_definitions',
                                         'flask_trigger_words.pyt')


def parse_section(iterator):
    """Parse a section of a file. Stops at empty line.

    Args:
        iterator(File): file descriptor pointing at a definition file.

    Returns:
         Iterator of all definitions in the section.
    """
    try:
        line = next(iterator).rstrip()
        while line:
            if line.rstrip():
                if SANITISER_SEPARATOR in line:
                    line = line.split(SANITISER_SEPARATOR)
                    sink = line[0].rstrip()
                    sanitisers = list(map(str.strip, line[1].split(',')))
                    yield (sink, sanitisers)
                else:
                    yield (line, list())
            line = next(iterator).rstrip()
    except StopIteration:
        return


def parse(trigger_word_file=default_trigger_word_file):
    """Parse the file for source and sink definitions.

    Returns:
       A definitions tuple with sources and sinks.
    """
    sources = list()
    sinks = list()
    with open(trigger_word_file, 'r') as fd:
        for line in fd:
            line = line.rstrip()
            if line == SOURCES_KEYWORD:
                sources = list(parse_section(fd))
            elif line == SINKS_KEYWORD:
                sinks = list(parse_section(fd))
    return Definitions(sources, sinks)
