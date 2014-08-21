#!/usr/bin/python
__author__ = 'Neil Parley'

from functools import wraps
import signal
import sys


def catch_sig(f):
    """
    Adds the signal handling as a decorator, define the signals and functions that handle them. Then wrap the functions
    with your decorator.
    :param f: Function
    :return: Function wrapped with registered signal handling
    """
    @wraps(f)
    def reg_signal(*args, **kwargs):
        def signal_handler(*args):
            print('Got killed')
            sys.exit(0)

        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGINT, signal_handler)
        return f(*args, **kwargs)

    return reg_signal


@catch_sig
def test():
    import time
    print("Waiting")
    time.sleep(60)

if __name__ == "__main__":
    test()