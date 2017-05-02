import logging


LOGGING_FMT = '%(levelname)3s] %(filename)s::%(funcName)s(%(lineno)d) - %(message)s'


def remove_other_handlers(to_keep=None):
    for hdl in logger.handlers:
        if hdl != to_keep:
            logger.removeHandler(hdl)


def enable_logger(to_file=None):
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler() if not to_file else logging.FileHandler(to_file, mode='w')
    ch.setLevel(logging.DEBUG)
    fmt = logging.Formatter(LOGGING_FMT)
    ch.setFormatter(fmt)
    logger.addHandler(ch)
    remove_other_handlers(ch)

logger = logging.getLogger('pyt')
remove_other_handlers()
