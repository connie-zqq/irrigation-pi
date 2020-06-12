import logging


def init_logging(level=logging.INFO):
    """ Initialize logging using the given level """
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # formater
    fmt = '%(asctime)s %(levelname)s %(name)s %(funcName)s : %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt)

    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # Turn off noisy logging
    logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)
    logging.getLogger("sh.command").setLevel(logging.WARNING)
