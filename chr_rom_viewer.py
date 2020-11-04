import pygame
import math
import numpy as np

WIDTH = int((256 * 5) / 2)
HEIGHT = 240 * 5 + 16*5

GRAY_SCALE = [(255, 255, 255), (170, 170, 170), (85, 85, 85), (0, 0, 0)]
# GRAY_SCALE = [(0, 0, 255), (255, 0, 0), (255, 255, 255), (210, 105, 30)]


def get_bit(byteval, idx):
    return (byteval&(1<<idx))

class Tile:
    def __init__(self, data):
        self.data = np.zeros(8, dtype=object)
        self.parse(data)

    def parse(self, data):
        for index, byte in enumerate(data):
            if index < 8:
                self.data[index] = np.array([int(bit) for bit in format(byte, '08b')])
            else:
                self.data[index%8] += np.array([int(bit)<<1 for bit in format(byte, '08b')])


    def draw(self, screen, offset_x=0, offset_y=0):
        for position_y, data in enumerate(self.data):
            for position_x, bit in enumerate(data):
                pygame.draw.rect(screen, GRAY_SCALE[bit], pygame.Rect(position_x*5+offset_x, position_y*5+offset_y, 5, 5))
                pass

class CHR_ROM_Viewer:

    def __init__(self):
        self.data = None
        self.index = 0

    def load(self, data):
        self.data = data

    def scan(self):
        tiles = []
        horizontal_tiles = WIDTH/(8*5) - 1

        for bank in self.data:
            tiles_data = np.split(bank, 512)
            tiles.append(Tile(tiles_data[0]))
            for tile_data in tiles_data:
                tiles.append(Tile(tile_data))

        horizontal_tile = 0
        vertical_tile = 0
        for index, tile in enumerate(tiles):
            if index > 0: #skipping first tile, not sure why no present in FCEUX emulator
                tile.draw(self.screen, horizontal_tile*8*5, vertical_tile*8*5)
                if horizontal_tile < horizontal_tiles:
                    horizontal_tile += 1
                else:
                    horizontal_tile = 0
                    vertical_tile += 1

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CHR ROM Viewer")
        self.running = True
        self.screen.fill((0, 0, 0))
        self.scan()
        pygame.display.flip()
        running = True
        while(running):
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
