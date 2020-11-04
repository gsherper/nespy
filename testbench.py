from bus import *
from cpu import *

cpu = CPU()
system_bus = Bus()
system_bus.connect_cpu(cpu)



test_read = cpu.read(0x0000)
print(test_read)
cpu.write(0x0000, 123)
print(cpu.read(0x0000))
print(cpu.read(0x0001))


