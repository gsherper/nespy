from nes import *
from chr_rom_viewer import *
import os
from instruction_set import *

nes = NES()

roms_dir = os.path.dirname(__file__)
rel_path = "roms/super_mario_bros.nes"
rom_file = os.path.join(roms_dir, rel_path)
nes.load_rom(rom_file)
nes.start()

chr_rom = nes.cart.get_chr_rom()

chr_viewer = CHR_ROM_Viewer()
chr_viewer.load(chr_rom)
chr_viewer.start()