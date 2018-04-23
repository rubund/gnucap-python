# Copyright (C) 2018 Felix Salfelder
# Author: Felix Salfelder <felix@salfelder.org>

# a simulation plugin written in python...
# load from gnucap with "python simplugin.py",
# then run "mysim".

from gnucap import install_command, SIM #, IO
import sys

class mysim(SIM):
	def do_it(self, cmd, scope):
		print("running mysim...")
		sys.stdout.flush()
	def setup(self, cmd):
		pass
		#out = IO.mstdout;
		#out.reset(); # BUG// don't know why this is needed
	def sweep(self):
		pass

sim = mysim()

d1 = install_command("test", sim)
#del(d1) #what does it do?
d1 = install_command("test", sim)

print("installing again")
d2 = install_command("test", sim)
print("installing again")
d3 = install_command("mysim", sim)

#BUG: that does not work as expected.
# it just breaks "mysim". why?
#d3 = install_command("mysim", sim)

sys.stdout.flush()
