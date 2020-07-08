import pygame

from src.globals import *


class Event_handler():

    def __init__(self, app, logika, panel, mobs=None):
        self.app = app
        self.logika = logika
        self.panel = panel
    
    def timer_run(self):
        self.logika.set_enemies()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.logika.gracz.moveup()
        elif keys[pygame.K_s]:
            self.logika.gracz.movedown()
        elif keys[pygame.K_a]:
            self.logika.gracz.moveleft()
        elif keys[pygame.K_d]:
            self.logika.gracz.moveright()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == 1:
                    self.logika.check_interactions(maps.get(self.logika.gracz.mmap).get_tile(int(mouse[0] / 32) - 8 + self.logika.gracz.x,
                                                                                int(mouse[1] / 32) - 8 + self.logika.gracz.y),
                                            self.panel, self.app, mouse)
                # panel.resolve(mouse, logika, app)
                # if maps.get(logika.gracz.mmap).get_tile(int(mouse[0]/32)-1,int(mouse[1]/32)-1).mob:
                # print(mapa.get_tile(int(mouse[0]/32)-1,int(mouse[1]/32)-1).mob.hp)
                # wywolaj funkcje wyswietlajaca informacje o mobie
                # if maps.get(logika.gracz.mmap).get_tile(int(mouse[0]/32)-1,int(mouse[1]/32)-1).mob.x != logika.gracz.x and maps.get(logika.gracz.mmap).get_tile(int(mouse[0]/32)-1,int(mouse[1]/32)-1).mob.y != logika.gracz.y:
                #    app.mob_pane = True
                # else:
                #    app.mob_pane = False
                elif event.button == 3:
                    '''right mouse button'''
                    pass

