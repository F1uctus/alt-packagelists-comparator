__version__ = "0.1.0"


def setup_logging():
    import sys
    import logging as log

    if sys.stdout.isatty():
        log.basicConfig(level=log.DEBUG)
    else:
        log.disable(log.WARNING)
