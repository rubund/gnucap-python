print("reading comp.py")

print("import gnucap")
import gnucap
print("done import gnucap")

from gnucap import component as c
from gnucap import install_device

try:
	a = gnucap.SIM()
	assert(False)
except RuntimeError:
	print("SIM construction refused (correctly)")

class MyAC(gnucap.SIM):
	def do_it(self, cmd, scope):
		print("HELLOWORLD")
	def setup(self, cmd):
		pass
	def sweep(self):
		pass

class MyAC2(gnucap.SIM):
	def do_it(self, cmd, scope):
		print("HELLOWORLD2")
	def setup(self, cmd):
		pass
	def sweep(self):
		pass

ac = MyAC()
ac2 = MyAC2()
print("install1")
d1 = gnucap.install_command("myac1", ac)
print("install2")
d2 = gnucap.install_command("myac", ac2)
d3 = gnucap.install_command("myac", ac)
d4 = gnucap.install_command("ac", ac)

gnucap.command("set trace")
gnucap.command("ac 1 2 * 2")
gnucap.command("myac1 1 2 * 2")
gnucap.command("myac:0 1 2 * 2")
gnucap.command("myac 1 2 * 2")

print("side effects")
# BUG?: weird side effects
del d2
gnucap.command("myac:0 1 2 * 2")
gnucap.command("myac 1 2 * 2")
gnucap.command("myac1 1 2 * 2")

print("done")

# gnucap.uninstall_command(d1)
# gnucap.uninstall_command(d2)
# gnucap.parse("myac 1 2 * 2")
