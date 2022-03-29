__version__ = "0.1.0"

import logging as log


def setup_logging(level=log.NOTSET):
    import sys

    if not level:
        level = log.NOTSET

    if sys.stdout.isatty():
        log.basicConfig(level=level)
    else:
        # Disable non-error logging if piped into another program.
        log.disable(log.WARNING)
