import os
import sys
import platform


if platform.architecture()[0] == "64bit":
    sysdir = "stdlib64"
else:
    sysdir = "stdlib"

sys.path.insert(0, os.path.join('better_ac', os.path.dirname(__file__), sysdir))
os.environ['PATH'] = os.environ['PATH'] + ";."


from .car import *
from .vectors import *
from .tyre import *
from .better_ac import *
