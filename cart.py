import numpy as np
from constants import *

HEADER_OFFSET = 16
HORIZONTAL = 0
VERTICAL = 1
FOURSCREEN = 2

def get_bit(byteval, idx):
    return ((byteval&(1<<idx))!=0)

class Cart:

    def __init__(self):
        print("Cart init")
        self.iNESFormat = False
        self.NES20Format = False
        self.rom_header = None
        self.rom_data = None
        self.prg_rom_size = 0
        self.chr_rom_size = 0
        self.flags_6 = 0
        self.flags_7 = 0
        self.flags_8 = 0
        self.flags_9 = 0
        self.flags_10 = 0
        self.prg_rom = []
        self.chr_rom = []

        self.mirroring_type = None
        self.battery_backed_ram = False
        self.trainer = False
        self.four_screen = False
        pass

    def check_NES_Format(self, header):
        assert header[0:3] == b'NES', "NES ROM Check failed"
        if header[0:4].decode() == "NES\x1a":
            self.iNESFormat = True
            if (header[7] & 0x0C) == 0x08:
                self.NES20Format = True

    def create_prg_rom(self):
        self.prg_rom = np.arange(self.prg_rom_size, dtype=object)
        for index, bank in enumerate(self.prg_rom):
            self.prg_rom[index] = np.zeros(KB16, dtype=np.uint8)

    def create_chr_rom(self):
        self.chr_rom = np.arange(self.chr_rom_size, dtype=object)
        for index, bank in enumerate(self.chr_rom):
            self.chr_rom[index] = np.zeros(KB8, dtype=np.uint8)

    def set_mirroring_type(self):
        if self.four_screen:
            self.mirroring_type = FOURSCREEN
        else:
            self.mirroring_type = VERTICAL if get_bit(self.flags_6, 0) else HORIZONTAL
        print("Mirroring type: ", MIRRORING_TYPE_DICT[self.mirroring_type])

    def set_battery_backed_ram(self):
        self.battery_backed_ram = True if get_bit(self.flags_6, 1) else False

    def set_trainer(self):
        self.trainer = True if  get_bit(self.flags_6, 2) else False

    def set_four_screen(self):
        self.four_screen = True if get_bit(self.flags_6, 3) else False

    def set_mapper(self):
        mask = 0b1111_0000
        lower_nibble = (self.flags_6 & mask) >> 4
        upper_nibble = (self.flags_7 & mask)
        self.mapper_id = upper_nibble + lower_nibble
        print("Mapper: ", mappers[self.mapper_id])
        pass

    def configure(self):
        self.create_prg_rom()
        self.create_chr_rom()
        self.set_four_screen()
        self.set_mirroring_type()
        self.set_battery_backed_ram()
        self.set_mapper()
        offset = self.populate_prg_rom(offset=0)
        self.populate_chr_rom(offset=offset)

    def populate_prg_rom(self, offset):
        return self.populate_rom(offset=offset, rom_type=self.prg_rom, bank_size=KB16)

    def populate_chr_rom(self, offset):
        return self.populate_rom(offset=offset, rom_type=self.chr_rom, bank_size=KB8)

    def populate_rom(self, offset, rom_type, bank_size):
        print(hex(offset))
        for bank in rom_type:
            for index, value in enumerate(bank):
                if offset + index > len(self.rom_data) - 1:
                    break
                bank[index] = self.rom_data[offset + index]
            offset += bank_size
        return offset

    def load(self, rom_data):
        self.rom_header = rom_data[0:15]
        self.rom_data = rom_data[HEADER_OFFSET:]
        self.check_NES_Format(self.rom_header)
        print("Loaded {rom}".format(rom=self.rom_header[0:3].decode()))
        self.prg_rom_size = self.rom_header[4] #16384 * x byte
        self.chr_rom_size = self.rom_header[5] #8192 * y bytes
        self.flags_6 = self.rom_header[6]
        self.flags_7 = self.rom_header[7]
        # self.flags_8 = self.rom_header[8]
        # self.flags_9 = self.rom_header[9]
        # self.flags_10 = self.rom_header[10]
        print("PRG ROM Size ", self.prg_rom_size)
        print("CHR ROM Size ", self.chr_rom_size)
        print("FLAGS6 ", self.flags_6)
        print("FLAGS7 ", self.flags_7)
        self.configure()
        pass

    def get_chr_rom(self):
        return self.chr_rom