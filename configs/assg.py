# imports
import m5
from m5.objects import *

# instantiating system
system = System()

# Set clock of instantiated system
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '3GHz'
system.clk_domain.voltage_domain = VoltageDomain()


