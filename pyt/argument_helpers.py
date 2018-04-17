import os
from argparse import ArgumentTypeError
from collections import namedtuple
from datetime import datetime
from enum import Enum


default_blackbox_mapping_file = os.path.join(
    os.path.dirname(__file__),
    'vulnerability_definitions',
    'blackbox_mapping.json'
)


default_trigger_word_file = os.path.join(
    os.path.dirname(__file__),
    'vulnerability_definitions',
    'all_trigger_words.pyt'
)


def valid_date(s):
    date_format = "%Y-%m-%d"
    try:
        return datetime.strptime(s, date_format).date()
    except ValueError:
        msg = "Not a valid date: '{0}'. Format: {1}".format(s, date_format)
        raise ArgumentTypeError(msg)


class UImode(Enum):
    INTERACTIVE = 0
    NORMAL = 1
    TRIM = 2


VulnerabilityFiles = namedtuple(
    'VulnerabilityFiles',
    (
        'blackbox_mapping',
        'triggers'
    )
)
