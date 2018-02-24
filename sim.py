print("reading comp.py")

print("import gnucap")
import gnucap
print("done import gnucap")

from gnucap import component as c
from gnucap.component import install_device

# BUG: this passes, although the constructor is protected
try:
	a = gnucap.sim()
	assert(False)
except RuntimeError:
	print("sim construction refused (correctly)")

class MyAC(gnucap.sim):
	def do_it(self, cmd, scope):
		print("HELLOWORLD")
	def setup(self, cmd):
		pass
	def sweep(self):
		pass

ac = MyAC()
d1 = gnucap.install_command("myac", ac)

# test: "already installed"
d2 = gnucap.install_command("myac", ac)

gnucap.command("ac 1 2 * 2")
gnucap.command("myac 1 2 * 2")

print("done")
