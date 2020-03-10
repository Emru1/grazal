from pygame_functions import *

class Player:
    sprite = pygame.sprite.Sprite

    def __init__(self, sprite):
        self.sprite = sprite

    def show(self):
        showSprite(self.sprite)

    def display(self, x, y):
        moveSprite(self.sprite, x, y)


class Szkielet(Player):
    pass
