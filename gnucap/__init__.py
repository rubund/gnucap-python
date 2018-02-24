# python3 only: use importlib

import sys
import ctypes
import os

# python tries to outsmart us, work around that
if(os.name=="posix"):
	flags = sys.getdlopenflags()
	sys.setdlopenflags(flags | ctypes.RTLD_GLOBAL)
	from gnucap_swig import *
	from component import component
	sys.setdlopenflags(flags)
else:
	untested()
	from gnucap_swig import *
	from component import component

# TODO: ask gnucap-conf (at configure time)
# BUG: do not override, if set.
os.environ["GNUCAP_PLUGPATH"] = "/usr/local/lib/gnucap"

if hasattr(sys, 'ps1'):
	print("welcome to gnucap-python")
	run_mode = SET_RUN_MODE(rINTERACTIVE)
else:
	run_mode = SET_RUN_MODE(rBATCH)
	if sys.flags.interactive:
		# what is this?
		print("... in interactive postmortem mode, incomplete")

try:
	lang = os.environ["GNUCAP_DEFAULT_PLUGINS"]
except:
	default_plugins = "gnucap-default-plugins.so"

try:
	lang = os.environ["GNUCAP_LANG"]
except:
	lang = "acs";

command("load " + default_plugins)
command("set lang=" + lang)

# this is the plan
# for s in simulations:
#	attach_output(s, our_own_sink)
