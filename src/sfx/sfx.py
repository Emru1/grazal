import random

import pygame


class SFX:
    def __init__(self):
        self.muz = ['sfx/muz1.ogg', 'sfx/muz2.ogg', 'sfx/muz3.ogg']

    def start(self):
        music = random.choice(self.muz)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

    def timer_run(self):
        if not pygame.mixer.music.get_busy():
            self.start()
