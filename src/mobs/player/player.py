from pygame_functions import *
from Box2D import *


class Player:
    sprite = pygame.sprite.Sprite

    def __init__(self, sprite, body):
        self.sprite = sprite
        self.body = body

    def show(self):
        showSprite(self.sprite)

    def move(self, x, y):
        moveSprite(self.sprite, x, y)


class Szkielet(Player):
    pass
