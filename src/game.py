import pygame
from map.map import Map


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    mapa = Map("mapa")

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    #move up
                elif event.key == pygame.K_s:
                    #move down
                elif event.key == pygame.K_a:
                    #move left
                elif event.key == pygame.K_d:
                    #move right
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    #Left mouse button
                elif event.button == 3:
                    #right mouse button 


if __name__ == "__main__":
    main()
