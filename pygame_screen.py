import pygame

WIDTH = 500
HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 0, 0))
running = True

while (running):
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 5, 5))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(500 - 5, 0, 5, 5))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 500 - 5, 5, 5))
    pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(500 - 5, 500 - 5, 5, 5))

    pygame.display.flip()