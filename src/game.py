import pygame
from map.map import Map
import globals


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    mapa = Map("mapa")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    #move up
                    pass
                elif event.key == pygame.K_s:
                    #move down
                    pass
                elif event.key == pygame.K_a:
                    #move left
                    pass
                elif event.key == pygame.K_d:
                    #move right
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #Left mouse button
                    pass
                elif event.button == 3:
                    #right mouse button
                    pass


if __name__ == "__main__":
    main()
