import pygame
from map.map import Map
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    mapa = Map("mapa")
    print(mapa.sizex)
    print(mapa.sizey)
    print(mapa.cell_size)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
