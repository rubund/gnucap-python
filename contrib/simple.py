import os
import numpy as np
import pylab

import gnucap

## Load custom plot command
import loadplot

## Load example circuit and run an ac analysis
gnucap.command("get example.ckt")
gnucap.command("store ac vm(2)")
gnucap.command("ac oct 10 1k 100k")

## Now use the new command to plot vm(2)
gnucap.command("myplot vm(2)")

