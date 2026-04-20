import os
from pathlib import Path
import sys

try:
    # can be imported if running the binary
    from sys import _MEIPASS

    RANDO_ROOT_PATH = Path(_MEIPASS)
    IS_RUNNING_FROM_SOURCE = False
except ImportError:
    RANDO_ROOT_PATH = Path(os.path.dirname(os.path.realpath(__file__)))
    IS_RUNNING_FROM_SOURCE = True

if getattr(sys, 'frozen', False):
    ROOT = Path(sys.executable).resolve().parent
else:
    ROOT = Path(__file__).resolve().parent
