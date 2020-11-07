from nes import *
import os
import pygame

WIDTH = 500
HEIGHT = 500

nes = NES()

roms_dir = os.path.dirname(__file__)
rel_path = "roms/super_mario_bros.nes"
rom_file = os.path.join(roms_dir, rel_path)
nes.load_rom(rom_file)
nes.start()

WHITE = (255, 255, 255)
font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)

def start():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("6502 RAM")
    screen.fill((0, 0, 0))
    running = True
    xcounter = 0
    ycounter = 0
    # for offset in range(20):
    #     data = hex(nes.bus.read(0x8000 + offset))
    #     draw_text(screen, data, 18, xcounter, ycounter)
    #     xcounter += 50
    #     if xcounter > 450:
    #         xcounter = 0
    #         ycounter += 50

    while running:
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        opcode = nes.emulate()
        if opcode is not None:
            draw_text(screen, hex(opcode), 18, xcounter, ycounter)
            xcounter += 50
            if xcounter > 450:
             xcounter = 0
             ycounter += 50

        pygame.display.flip()

    pygame.quit()

start()


