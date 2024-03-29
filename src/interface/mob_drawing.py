import pygame

from src.globals import *
from src.map.tile import Tile


class MobSurface:
    """
    Powierzchnia o wymiarach obliczonych z configu.
    Funkcja draw(x, y) przyjmuje pozycje wyrazona w koordynatach mapy na srodek ekranu,
    nastepnie przygotowywuje i zwraca powierzchnie z dorysowanymi mobami
    """

    def __init__(self, mapa):
        self.map_grid = [[Tile() for _ in range(config.grid_x)] for _ in range(config.grid_y)]
        self.mapa = mapa
        self.surface = pygame.Surface((config.grid_x * config.tile_size, config.grid_y * config.tile_size))
        self.shadow = asset.get('shadow')

    def __get_tiles(self, x, y):
        x = x - int(config.grid_x / 2)
        y = y - int(config.grid_y / 2)
        for i in range(config.grid_x):
            for j in range(config.grid_y):
                self.map_grid[i][j] = self.mapa.get_tile(i + x, j + y)

    def __draw_tile(self, surface, x, y):
        if self.map_grid[x][y]:
            if self.map_grid[x][y].mob:
                img = asset.get(self.map_grid[x][y].mob.asset)
                surface.blit(self.shadow, (x * config.tile_size, y * config.tile_size))
                surface.blit(img, (x * config.tile_size, y * config.tile_size))

    def draw(self, surface, x, y):
        """
        rysuje siatke mapy z centrum podanym w parametrach x, y

        :param surface: pygame.Surface
        :param x: int
        :param y: int
        :return: pygame.surface
        """
        self.__get_tiles(x, y)
        for i in range(config.grid_x):
            for j in range(config.grid_y):
                self.__draw_tile(surface, i, j)
        return surface
