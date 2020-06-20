from src.globals import *
from src.map.map import Map
from src.map.tile import Tile
import pygame

"""
Powierzchnia o wymiarach obliczonych z configu
funkcja draw(x, y) przyjmuje pozycje wyrazona w koordynatach mapy na srodek ekranu
nastepnie przygotowywuje i zwraca powierzchnie do narysowania na ekranie
"""


class MapSurface:

    def __init__(self, mapa):
        self.map_grid = [[Tile() for x in range(config.grid_x)] for y in range(config.grid_y)]
        self.mapa = mapa
        self.surface = pygame.Surface((config.grid_x * config.tile_size, config.grid_y * config.tile_size))

    def __get_tiles(self, x, y):
        x = x - config.grid_x/2
        y = y - config.grid_y/2
        for i in range(0, config.grid_x):
            for j in range(0, config.grid_y):
                self.map_grid[i][j] = self.mapa.get_tile(i, j)

    def __draw_tile(self, x, y):
        if self.map_grid[x][y]:
            img = asset.get(self.map_grid[x][y].asset)
        else:
            img = "black"
        to_draw = asset.get(img)
        self.surface.blit(to_draw, (x * config.tile_size, y * config.tile_size))

    def draw(self, x, y):
        self.map_grid.clear()
        self.surface.fill([0, 0, 0])
        self.__get_tiles(x, y)
        for i in range(config.grid_x):
            for j in range(config.grid_y):
                self.__draw_tile(i, j)
        return self.surface
