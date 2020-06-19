import pygame


class Asset:
    def __init__(self):
        self.imgs = {}

    def add(self, name, path):
        self.imgs[name] = pygame.image.load("img/" + path)

    def convert(self):
        for x in self.imgs:
            x.convert()
