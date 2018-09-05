from __future__ import print_function

import sys
import ctypes
import os

def trace(*args, **kwargs):
	   print(*args, file=sys.stderr, **kwargs)

ctypes.PyDLL("libgnucap.so", mode=ctypes.RTLD_GLOBAL)

oldflags = sys.getdlopenflags()
if(os.name=="posix"):
	# python tries to outsmart us, work around that
	trace("POSIX ON")
	sys.setdlopenflags(oldflags | ctypes.RTLD_GLOBAL)
	trace("PYDDL'd")
else:
	untested()

from .gnucap_swig import command, parse
trace("cmd imported")
from .c_comand import CMD, CMD_cmdproc, CMD_command
from .c_exp import eval
from .component import COMPONENT_ as COMPONENT
from .e_base import CKT_BASE_find_wave, CKT_BASE
from .e_cardlist import CARD_LIST
from .e_elemnt import ELEMENT
from .e_node import node_t
from .m_cpoly import FPOLY1, CPOLY1
from .md import rBATCH, rINTERACTIVE, rPRESET, rPRE_MAIN, rSCRIPT
from .md import ENV
from .m_matrix import BSMATRIXd, BSMATRIXc
from .m_wave import WAVE
from .s__ import SIM_ as SIM
from .u_opt import SET_RUN_MODE
from .u_sim_data import SIM_DATA

from ._io_ import OMSTREAM__print, IO_mstdout_get

_iomstout = IO_mstdout_get()

def out(s):
	OMSTREAM__print(_iomstout, s)

if(os.name=="posix"):
	sys.setdlopenflags(oldflags)

# this will change
from .globals import install_device, need_default_plugins
from .globals import install_command
# from globals import shared_command_installer as command_installer

if not "GNUCAP_PLUGPATH" in os.environ:
	os.environ["GNUCAP_PLUGPATH"] = "/usr/local/lib/gnucap"

if hasattr(sys, 'ps1'):
	trace("welcome to gnucap-python")
	run_mode = SET_RUN_MODE(rINTERACTIVE)
else:
	run_mode = SET_RUN_MODE(rBATCH)
	if sys.flags.interactive:
		# what is this?
		trace("... in interactive postmortem mode, incomplete")

try:
	lang = os.environ["GNUCAP_DEFAULT_PLUGINS"]
except:
	default_plugins = "gnucap-default-plugins.so"

try:
	lang = os.environ["GNUCAP_LANG"]
except:
	lang = "acs";

if need_default_plugins():
	# no c_python. likely "import gnucap"
	trace("loading default plugins")
	command("load " + default_plugins)
	command("set lang=" + lang)
else:
	trace("from c_python")
	# calling pythonstuff from c_python?
	pass

#c_python = True

# this is the plan
# for s in simulations:
#	attach_output(s, our_own_sink)

class session:
	def __del__(self):
		# this is called *before* the library loaded by PyDLL is destroyed.
		trace("cleaning up")
		command("clear")
		trace("cleanup done")

s = None
if(sys.version_info[0] == 3):
	trace("making session")
	s = session()
else:
	# TODO: don't know how to call clear at the end in python 2.
	# this results in a garbage collector assertion in gnucap (if assertions are active)
	pass

