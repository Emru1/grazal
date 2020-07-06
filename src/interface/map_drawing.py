import pygame

from src.globals import *
from src.map.tile import Tile


class MapSurface:
    """
    Powierzchnia o wymiarach obliczonych z configu.
    Funkcja draw(x, y) przyjmuje pozycje wyrazona w koordynatach mapy na srodek ekranu,
    nastepnie przygotowywuje i zwraca powierzchnie do narysowania na ekranie
    """

    def __init__(self, mapa):
        self.map_grid = [[Tile() for _ in range(config.grid_x)] for _ in range(config.grid_y)]
        self.mapa = mapa
        self.surface = pygame.Surface((config.grid_x * config.tile_size, config.grid_y * config.tile_size))
        self.lx = -1
        self.ly = -1

    def __get_tiles(self, x, y):
        x = x - int(config.grid_x / 2)
        y = y - int(config.grid_y / 2)
        for i in range(config.grid_x):
            for j in range(config.grid_y):
                self.map_grid[i][j] = self.mapa.get_tile(i + x, j + y)

    def __draw_tile(self, x, y):
        if self.map_grid[x][y]:
            img = asset.get(self.map_grid[x][y].asset)
        else:
            img = "black"
        self.surface.blit(img, (x * config.tile_size, y * config.tile_size))

    def draw(self, x, y):
        """
        rysuje siatke mapy z centrum podanym w parametrach x, y

        :param x: int
        :param y: int
        :return: pygame.surface
        """
        if self.lx == x and self.ly == y:
            return self.surface
        self.lx = x
        self.ly = y
        self.surface.fill([0, 0, 0])
        self.__get_tiles(x, y)
        for i in range(config.grid_x):
            for j in range(config.grid_y):
                self.__draw_tile(i, j)
        return self.surface
