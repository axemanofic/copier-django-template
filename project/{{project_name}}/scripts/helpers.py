from typing import List
import sys
import subprocess
import functools

from .config import CWD


class Context:
    def __init__(self, argv: List[str] = None):
        self.argv = argv

    def run(self, cmds: List[str]):
        p = subprocess.Popen(cmds + self.argv, cwd=CWD)
        try:
            p.wait()
        except KeyboardInterrupt:
            p.terminate()


def task():
    def decorator(func):
        @functools.wraps(func)
        def wrapper():
            ctx = Context(argv=sys.argv[1:])
            return func(ctx)

        return wrapper

    return decorator
