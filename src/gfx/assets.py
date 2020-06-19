import pygame


class Asset:
    def __init__(self):
        self.imgs = {}
        asset_file = open("cfg/asset_list.txt")
        line_num = 0
        for line in asset_file:
            line_num += 1
            line = line.splitlines()[0]
            line = line.lstrip(' ')
            if line[0] == '#':
                continue
            self.imgs[str(line.split(' ')[0])] = pygame.image.load("img/" + str(line.split(' ')[1]))

    def add(self, name, path):
        if name in self.imgs:
            print("Bylo")
            return
        self.imgs[name] = pygame.image.load("img/" + path)

    def get(self, name):
        return self.imgs[name]

    def convert(self):
        for x in self.imgs:
            x.convert()
