from collections import namedtuple
from enum import Enum


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
