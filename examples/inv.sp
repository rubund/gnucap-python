spice
*Digital inverter
* .INCLUDE tsmc018.m
.include p.typ
.include n.typ


*** *** SUPPLY VOLTAGES *** ***
VDD ndd 0 V_SUPPLY
VSS VSS 0 0

*** *** INPUT SIGNAL *** ***
VSIG IN VSS PULSE V_SUPPLY 0 'INP_PERIOD/2' 'INP_PERIOD/1000'
+               'INP_PERIOD/1000' 'INP_PERIOD/2' 'INP_PERIOD'

*** *** CIRCUIT *** ***
MP OUT IN ndd ndd mypmos W=WP   L=LMIN
MN OUT IN VSS VSS mynmos W='WP/3' L=LMIN

CL OUT VSS 10p

.PARAM INP_PERIOD = '1/INP_FREQ'
.PARAM NO_PERIODS = '4'
.PARAM TMEAS_START = '(NO_PERIODS-1)*INP_PERIOD'
.PARAM TMEAS_STOP = '(NO_PERIODS)*INP_PERIOD'
.PARAM TMEAS_1 = 'TMEAS_STOP -3*INP_PERIOD/4'
.PARAM TMEAS_2 = 'TMEAS_STOP -1*INP_PERIOD/4'

.param stepsize = 'INP_PERIOD/100'
.param tend = 'NO_PERIODS*INP_PERIOD'

*** *** PARAMS *** ***
.param V_SUPPLY = 2.000000
.param TEMP = 25.000000
.param LMIN = 0.000001
.param INP_FREQ = 850000000.000000
.param WP = 0.007963
*** *** ANALYSIS *** ***

.store tran i(vdd) v(out)
.op
.mark
.end
