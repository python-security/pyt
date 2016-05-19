"""A setup module for loggin."""
import logging
from collections import OrderedDict

separator = ' | '
log_formats = (('Date', '%(asctime)s'), ('path', '%(pathname)s'), ('filename', '%(filename)s'), ('module', '%(module)s'), ('line', '%(lineno)d'), ('function', '%(funcName)s'), ('level', '%(levelname)s'), ('message', '%(message)s'))
log_format_dict = OrderedDict(log_formats)

def get_level(level):
    """Convert string level to int level value."""
    if level == None:
        #Default level=WARNING
        return 30
        
    level = level.upper()
    if level == 'CRITICAL':
        return 50
    elif level == 'ERROR':
        return 40
    elif level == 'WARNING':
        return 30
    elif level == 'INFO':
        return 20
    elif level == 'DEBUG':
        return 10
    elif level == 'NOTSET':
        return 0
    else:
        raise TypeError('Unknown level type, should be: CRITICAL, ERROR, WARNING(Default), INFO, DEBUG or NOTSET. Level value is: ', level)
        
def set_logger(level, show_path=True):
    """Set the logger values and what should be shown as output in the logfile."""
    level = get_level(level)
    if not show_path:
        log_format_dict.pop('path')
    logging.basicConfig(filename='logger.log', level=level, format=separator.join(log_format_dict.values()))
    logger = logging.getLogger(__name__)
    logger.info('FORMAT: ' + separator.join(log_format_dict.keys()))
    logger.info('Logging has been started.')

