from nes import *
import os


nes = NES()

roms_dir = os.path.dirname(__file__)
rel_path = "roms/galaga.nes"
rom_file = os.path.join(roms_dir, rel_path)
nes.load_rom(rom_file)