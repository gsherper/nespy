import numpy as np

HORIZONTAL = 0
VERTICAL = 0

class Cart:

    def __init__(self):
        print("Cart init")
        self.iNESFormat = False
        self.NES20Format = False
        self.data = bytes()
        self.rom_header = bytes()
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
        pass

    def check_NES_Format(self, header):
        assert header[0:3] == b'NES', "NES ROM Check failed"
        if header[0:4].decode() == "NES\x1a":
            self.iNESFormat = True
            if (header[7] & 0x0C) == 0x08:
                self.NES20Format = True

    def create_prg_rom(self):
        self.prg_rom = []
        for bank in range(self.prg_rom_size):
            self.prg_rom.append(np.zeros(16384, dtype=np.uint8))

    def create_chr_rom(self):
        self.chr_rom = []
        for bank in range(self.chr_rom):
            self.chr_rom[bank] = np.zeros(8192, dtype=np.uint8)

        print(self.chr_rom)

    def set_mirroring_type(self):
        if self.flags_6[0]:
            self.mirroring_type = VERTICAL
        else:
            self.mirroring_type = HORIZONTAL

        print("mirroring type ", self.mirroring_type)

    def configure(self):
        self.create_prg_rom()
        self.create_chr_rom()
        self.set_mirroring_mode()

    def load(self, rom_data):
        self.rom_header = rom_data[0:15]
        self.check_NES_Format(self.rom_header)
        print("Loaded {rom}".format(rom=self.rom_header[0:3].decode()))
        self.prg_rom_size = self.rom_header[4] #16384 * x byte
        self.chr_rom_size = self.rom_header[5] #8192 * y bytes
        self.flags_6 = self.rom_header[6]
        self.flags_7 = self.rom_header[7]
        self.flags_8 = self.rom_header[8]
        self.flags_9 = self.rom_header[9]
        self.flags_10 = self.rom_header[10]
        print("PRG ROM Size ", self.prg_rom_size)
        print("CHR ROM Size ", self.chr_rom_size)
        print("FLAGS6 ", self.flags_6)
        print("FLAGS7 ", self.flags_7)
        print("FLAGS8 ", self.flags_8)
        print("FLAGS9 ", self.flags_9)
        print("FLAGS10 ", self.flags_10)

        self.configure()

        pass