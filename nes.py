from cart import *

class NES:

    def __init__(self):
        print("NES Init")
        self.cart = Cart()
        pass

    def load_rom(self, file_name):

        with open(file_name, mode='rb') as file:
            rom = file.read()
            self.cart.load(rom)
        pass


