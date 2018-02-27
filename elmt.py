# Copyright (C) 2018 Felix Salfelder
# Author: Felix Salfelder <felix@salfelder.org>

import gnucap

from gnucap import ELEMENT
from gnucap import node_t
from gnucap import install_device
from copy import deepcopy, copy

try:
	c = ELEMENT()
	print("ERROR, must be pure")
	assert(False)
except RuntimeError:
	pass
except AttributeError:
	pass

# trick python garbage collector
# todo: hide in wrapper layer

class someelt(ELEMENT):
	def __init__(self, other=None):
		if other is None:
			print("construct someelt", self)
			ELEMENT.__init__(self) # this is required. (or do not implement __init__)
		else:
			print("copyconstruct someelt")
			ELEMENT.__init__(self, other) # this is required. (or do not implement __init__)
		print("init", self.long_label())
		self.HACK=[]

#	def __reduce__(self):
#		print("reducing")
#		return(self.__class__, ( ) )

	def clone(self):
		print("somelt clone")
		x = someelt(self)
		self.HACK.append(x)
		return x

	def value(self):
		return "a";

	def dev_type(self):
		return "pyelt"

	def min_nodes(self):
		print("min");
		return 2;
	def net_nodes(self):
		return 2;
	def max_nodes(self):
		print("max");
		return 2;
	def net_nodes(self):
		return 2;
	def tr_iwant_matrix(self):
		print("iwant incomplete")
	def ac_iwant_matrix(self):
		print("iwant incomplete")

	def tr_involts(self):
		return self.tr_outvolts()

	def tr_probe_num(self, s):
		if s=="fourtytwo":
			return 42;
		elif s=="v":
			return self.tr_involts()
		elif s=="nodeprobe":
			# this is a bit ugly :|
			return gnucap.e_node.get_node(self._n,0).v0()
		return 0;


	def port_number(self):
		return 2
	def port_name(self,x):
		return ["P","N"][x]
	def value_name(self):
		return "incomplete"

s = someelt()
print("mtest", s.max_nodes(), s.long_label())
s2 = s.clone()
print("mtest", s2.max_nodes(), s2.long_label())
# s.clone()

print("TT", type(s))
a = install_device("someelt", s)
# b = gnucap.command_installer("someelt", s)

gnucap.command("set lang=verilog")
gnucap.parse("vsource #(.dc(1)) v(1 0)")
gnucap.parse("someelt #() s(1 0)")
gnucap.command("list")
gnucap.command("print dc fourtytwo(s) v(s) nodeprobe(s)")
gnucap.command("dc v 0 1 .5")

print("done")
