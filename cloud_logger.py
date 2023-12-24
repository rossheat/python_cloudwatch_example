import logging
from watchtower import CloudWatchLogHandler
import sys


def logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        f"%(levelname)s - %(message)s (%(filename)s:%(funcName)s:%(lineno)d)",
    )

    cw_handler = CloudWatchLogHandler(
        log_group="python_cloudwatch_example",
        stream_name="my_logs_stream_name",
    )

    cw_handler.setFormatter(formatter)
    logger.addHandler(cw_handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
