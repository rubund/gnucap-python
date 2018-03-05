"""
Copyright: 2009-2011 Henrik Johansson
Author: Henrik Johansson

Create a new ac-analysis that always runs at a single frequency
"""

import os
import numpy as np
import pylab

import gnucap

cl=gnucap.CARD_LIST().card_list_()

print("MYAC")
A=file("/tmp/HELLO","w+")

gnucap.command("set trace")
gnucap.command("set lang=acs")

## Set gnucap run mode
runmode = gnucap.SET_RUN_MODE(gnucap.rBATCH)

gnucap.command("get example.ckt")

class MyAC(gnucap.SIM):
    def do_it(self, cmd, scope):
        self._scope = scope
        self.sim_().set_command_ac()
        self.sim_().init()
        self.sim_().alloc_vectors()
        acx = self.sim_()._acx
        acx.reallocate()

        freq = 20e3

        self.sim_()._jomega = 2j * np.pi * freq

#        self.head(freq, freq, "Freq")

        card_list = gnucap.CARD_LIST().card_list_()
        card_list.ac_begin()
        print("begun")

        self.solve()
        print("solved")

        self.outdata(freq)

        acx.unallocate();
        self.unalloc_vectors()

    def solve(self):
        acx =  gnucap.cvar.CKT_BASE_acx ## Static attributes must be accessed through cvar
        acx.zero()
        card_list = gnucap.cvar.CARD_LIST_card_list
        
        ## Total number of states
        n = gnucap.cvar.status.total_nodes

#        gnucap.set_complex_array(gnucap.cvar.SIM_ac, np.zeros(n, dtype=np.complex))
        
        card_list.do_ac()
        card_list.ac_load()

        print "Loaded AC-matrix", gnucap.get_complex_array(gnucap.cvar.SIM_ac, n)

        print gnucap.bsmatrix_to_array_c(acx)

        ## Solve
        acx.lu_decomp()
        acx.fbsub(gnucap.cvar.SIM_ac)
   
        print "rhs after", gnucap.get_complex_array(gnucap.cvar.SIM_ac, n)

               
    def setup(self, cmd):
        pass
    def sweep(self):
        pass

myac = MyAC()

d0=gnucap.install_command("myac", myac)
d1=gnucap.install_command("ac", myac)

gnucap.command("store ac vm(2)")
gnucap.command("myac")

w= gnucap.SIM.find_wave("vm(2)")
x,y = gnucap.wave_to_arrays(w)
print x,y
