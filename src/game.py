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


if __name__ == "__main__":
    main()
