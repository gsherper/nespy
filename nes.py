from cart import *
from cpu import *
from bus import *

class NES:

    def __init__(self):
        print("NES Init")
        self.cart = Cart()
        self.bus = Bus()
        self.cpu = CPU()
        pass

    def load_rom(self, file_name):
        with open(file_name, mode='rb') as file:
            rom = file.read()
            self.cart.load(rom)

    def start(self):
        self.bus.connect_device(self.cart)
        self.cart.load_to_memory()
        self.bus.connect_device(self.cpu)
        self.cpu.reset()

    def emulate(self):
        return self.cpu.clock()
