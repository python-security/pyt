from argparse import ArgumentTypeError
from datetime import datetime


def valid_date(s):
    date_format = "%Y-%m-%d"
    try:
        return datetime.strptime(s, date_format).date()
    except ValueError:
        msg = "Not a valid date: '{0}'. Format: {1}".format(s, date_format)
        raise ArgumentTypeError(msg)
