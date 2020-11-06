import numpy as np

class Bus:

    def __init__(self):
        # Devices
        # 6502
        self.cpu = None
        # 64 KB Ram
        self.ram = np.zeros(64*1024, dtype=int)

    def connect_device(self, device):
        # self.cpu = cpu
        device.bus = self

    def write(self, address, data):
        if 0x0000 <= address <= 0xFFFF:
            self.ram[address] = data
        pass

    def read(self, address, read_only=False):
        if 0x0000 <= address <= 0xFFFF:
            return 0x25
            #return self.ram[address]
        else:
            return 0x00
        pass

