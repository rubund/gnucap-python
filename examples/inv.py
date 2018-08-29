# ASCO replacement
# (C) 2018 Felix Salfelder
# GPLv3

# use gnucap to evaluate target functions for nlopt. example similar to "inv"
# in the ASCO manual.

# this is part of gnucap-python

import sys
import numpy as np
import gnucap
from gnucap import command
import nlopt

def setup_circuit():
	command("get inv.sp")
	command("store op v(nodes)")
	command("print op v(nodes)")
	command("store tran v(nodes) i(vdd)")

# run gnucap. measure data
# this is what ASCO does in extract/*
def eval(V_SUPPLY=2., LMIN=0.000001, INP_FREQ=850000000., WP=.007963, TEMP=25.):
	if np.isnan(V_SUPPLY):
		raise ValueError()

	command("param V_SUPPLY="+str(V_SUPPLY))
	command("transient 'INP_PERIOD/100' 'NO_PERIODS*INP_PERIOD' > x")

	command('measure ZP_SUPPLY0 rms(probe="I(VDD)" begin=tmeas_start end=tmeas_stop)>/dev/null')
	command("measure ZVHIGH1 at(probe='v(OUT)' at='TMEAS_2')>/dev/null")
	command("measure ZVLOW2  at(probe='v(OUT)' at='TMEAS_1')>/dev/null")

	zps = gnucap.eval("ZP_SUPPLY0")
	zvhigh = gnucap.eval("ZVHIGH1")
	zvlow = gnucap.eval("ZVLOW2")

	return zps, zvhigh, zvlow

# all callbacks require the results. only evaluate once per point.
hackresult = []
hackx = 0
def eval_cache(*args):
	global hackresult
	global hackx

	if(args!=hackx):
		hackx = args
		hackresult = eval(*args)

	return hackresult

setup_circuit()

n = 4
opt = nlopt.opt(nlopt.LN_COBYLA, n)

# does not work with ineuality constraints
# opt = nlopt.opt(nlopt.LN_BOBYQA, n)

# ASCO: VLOW:OUT:LE:0.05:sometran:
def boundarylow(result, x, grad):
	assert(grad.size==0)
	e = eval_cache(*x)
	result[0] = e[2] + 0.05
opt.add_inequality_mconstraint(boundarylow, [1e-10])

# ASCO: VHIGH:OUT:GE:1.95:sometran:
def boundaryhigh(result, x, grad):
	assert(grad.size==0)
	e = eval_cache(*x)
	result[0] = 1.95 - e[1]
opt.add_inequality_mconstraint(boundaryhigh, [1e-10])

opt.set_lower_bounds([2., 1e-9, 10., 0.0001])
opt.set_upper_bounds([2.01, 1e-3, 1e9, 1] )

# ASCO: P_SUPPLY:---:MIN:0:sometran:
def objective(x, grad):
	assert(grad.size==0)
	e = eval_cache(*x)
	return e[0]
opt.set_min_objective(objective)

# tolerances. this does not really matter here (too simple)
opt.set_xtol_abs([1e-15] * 4);
opt.set_xtol_rel(1e-20);

# do it
xopt = opt.optimize([2.,0.0002,1000.,0.1])

print("optimum:")
print("V_SUPPLY: ", xopt[0])
print("LMIN: ", xopt[1])
print("FREQ: ", xopt[2])
print("WP: ", xopt[3])

# sometimes crashes during shutdown.
print("done")
