import pygame

from src.globals import *


def event_handler(app, logika, mmap, panel, mobs=None):
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        '''move up'''
        logika.gracz.moveup()
        logika.set_enemies()
    elif key[pygame.K_s]:
        logika.gracz.movedown()
        logika.set_enemies()
        '''move down'''
    elif key[pygame.K_a]:
        logika.gracz.moveleft()
        logika.set_enemies()
        '''move left'''
    elif key[pygame.K_d]:
        logika.gracz.moveright()
        logika.set_enemies()
        '''move right'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if event.button == 1:
                logika.check_interactions(maps.get(logika.gracz.mmap).get_tile(int(mouse[0] / 32) - 8 + logika.gracz.x,
                                                                               int(mouse[1] / 32) - 8 + logika.gracz.y),
                                          panel, app, mouse)
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
