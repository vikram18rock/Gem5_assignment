# imports
import m5
from m5.objects import *

# instantiating system
system = System()

# Set clock of instantiated system
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '3GHz'
system.clk_domain.voltage_domain = VoltageDomain()

# creating 4GB main memory
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('4GB')]

# setting OoO cpu for the system
system.cpu = DerivO3CPU()

# Create a Memoybus to connect cpu to memory
system.membus = SystemXBar()
