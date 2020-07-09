import pygame
import random


class SFX:
    def __init__(self):
        self.muz = ['sfx/muz1.ogg', 'sfx/muz2.ogg', 'sfx/muz3.ogg']

    def start(self):
        music = random.choice(self.muz)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

