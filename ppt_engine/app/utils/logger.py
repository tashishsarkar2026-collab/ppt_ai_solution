"""
Centralized project logger.
"""

import logging


def setup_logger():

    logger = logging.getLogger("ppt_engine")

    # Prevent duplicate logs
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        (
            "[%(asctime)s] "
            "[%(levelname)s] "
            "%(message)s"
        ),
        datefmt="%H:%M:%S"
    )

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


logger = setup_logger()