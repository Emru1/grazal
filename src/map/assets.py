import pygame


class Asset:
    def __init__(self):
        self.img = pygame.image

    def init(self, path):
        path = "img/" + path
        self.img = pygame.image.load(path)

    def convert(self):
        self.img.convert()