# imports
import m5
from m5.objects import *
# import custom classes from caches module
from caches import *

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
system.cpu = X86TimingSimpleCPU()

# Create a Memoybus to connect cpu to memory
system.membus = SystemXBar()

# Create Cache simObjects
system.cpu.icache = L1ICache()
system.cpu.dcache = L1DCache()

# Connect cpu to cachePorts
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

# Create a bus to connect L1Cache with L2Cache
system.l2bus = L2XBar()

system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

# Connect an I/O Controller
system.cpu.createInterruptController()
# Exclusive for X86
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports
# pio       - Parallel input output Controller
# requestor - membus port to request from cpu
# responder - membus port to respond for cpu

# Important system_port, functional port
# Allows read and write of memory by system
system.system_port = system.membus.cpu_side_ports

# Add Memctrl unit as well
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# -------------------- SIMULATION ---------------------- #
"""
    # Create a process
    # Point it to the compiled binary
"""

# process creation
# point to binary
thispath = os.path.dirname(os.path.realpath(__file__))
binary = os.path.join(
    thispath,
    "hello"
)

system.workload = SEWorkload.init_compatible(binary)

process = Process()
process.cmd = [binary]
system.cpu.workload = process
system.cpu.createThreads()

"""
    # All simObjects are children to Root simObject
    # only children of Root simObject are instantiated during a SIMULATION
"""
root = Root(full_system = False, system = system)

# instantiate the SIMULATION
m5.instantiate()

# Simulate the script
m5.simulate()
