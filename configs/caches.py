# import objects from Cache.py module
from m5.objects import Cache

""" 
    # Cache class is the standard class
    # Any cache is an inheritance of this class
    # we create
    #
    #       Cache
    #           |
    #       L1Cache
    #           |
    #       ---------
    #       |       |
    #   L1ICache    L1DCache
"""

# Adding the non default variable values of base class Cache
class L1Cache(Cache):
    # 4 way assosciativity
    assoc = 4
    
    # for 3 cycle latency over a cache hit
    tag_latency = 1
    data_latency = 1
    response_latency = 1
    # 1 + 1 + 1 = 3
    # miss-status-holding-registers
    mshrs = 32
    tgts_per_mshr = 20

    def connectCPU(self, cpu):
    # need to define this in a base class!
        raise NotImplementedError

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports

class L1ICache(L1Cache):
    size = '32kB'

    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port

class L1DCache(L1Cache):
    size = '32kB'

    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port
