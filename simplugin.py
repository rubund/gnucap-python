# Copyright (C) 2018 Felix Salfelder
# Author: Felix Salfelder <felix@salfelder.org>

from gnucap import install_command, SIM

class mysim(SIM):
	def do_it(self, cmd, scope):
		print("running mysim...")
	def setup(self, cmd):
		pass
	def sweep(self):
		pass

sim = mysim()
print("installing mysim")

# BUG: when is d1 going to be destroyed?!
d1 = install_command("mysim", sim)
