import logging
from collections import OrderedDict

separator = ' | '
log_formats = (('Date', '%(asctime)s'), ('path', '%(pathname)s'), ('filename', '%(filename)s'), ('module', '%(module)s'), ('line', '%(lineno)d'), ('function', '%(funcName)s'), ('level', '%(levelname)s'), ('message', '%(message)s'))
log_format_dict = OrderedDict(log_formats)
logger = None

def set_logger(logger):
    logger = logger
    return logger

def get_level(level):
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
        
def get_logger(level, name, show_path=True):
    if logger:
        return logger
    level = get_level(level)
    if not show_path:
        log_format_dict.pop('path')
    logging.basicConfig(filename='logger.log', level=level, format=separator.join(log_format_dict.values()))
    l = set_logger(logging.getLogger(name))
    l.info('FORMAT: ' + separator.join(log_format_dict.keys()))
    l.info('Logging has been started.')
    return l

