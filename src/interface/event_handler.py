import pygame

from src.globals import *


class Event_handler:

    def __init__(self, app, logika, panel, mobs=None):
        self.app = app
        self.logika = logika
        self.panel = panel
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def check_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.up = True
        elif keys[pygame.K_s]:
            self.down = True
        elif keys[pygame.K_a]:
            self.left = True
        elif keys[pygame.K_d]:
            self.right = True

    def timer_run(self):
        self.logika.set_enemies()
        if self.up:
            self.logika.gracz.moveup()
        elif self.down:
            self.logika.gracz.movedown()
        elif self.left:
            self.logika.gracz.moveleft()
        elif self.right:
            self.logika.gracz.moveright()

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == 1:
                    self.logika.check_interactions(maps.get(self.logika.gracz.mmap).get_tile(
                        int(mouse[0] / 32) - 8 + self.logika.gracz.x, int(mouse[1] / 32) - 8 + self.logika.gracz.y),
                        self.panel, self.app, mouse)

                elif event.button == 3:
                    '''right mouse button'''
                    pass
