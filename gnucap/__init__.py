# python3 only: use importlib

import sys
import ctypes

flags = sys.getdlopenflags()
sys.setdlopenflags(flags | ctypes.RTLD_GLOBAL)
from _gnucap import *
sys.setdlopenflags(flags)

# TODO: ask gnucap-conf (at configure time)
import os
os.environ["GNUCAP_PLUGPATH"] = "/usr/local/lib/gnucap"

# not so sure. depend on variables in rc
ENV_run_mode_set(rBATCH)
command("load gnucap-default-plugins.so")
command("set lang acs")

print("welcome to gnucap-python")
