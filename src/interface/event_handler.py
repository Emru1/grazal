import pygame
from src.globals import *

def event_handler(app,logika,map,panel,mobs=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                '''move up'''
                logika.gracz.moveup()
            elif event.key == pygame.K_s:
                logika.gracz.movedown()
                '''move down'''
            elif event.key == pygame.K_a:
                logika.gracz.moveleft()
                '''move left'''
            elif event.key == pygame.K_d:
                logika.gracz.moveright()
                '''move right'''
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if event.button == 1:
                print(mouse[0],mouse[1])
                panel.resolve(mouse,logika,app)
                #if maps.get(logika.gracz.mmap).get_tile(int(mouse[0]/32)-1,int(mouse[1]/32)-1).mob:
                    #print(mapa.get_tile(int(mouse[0]/32)-1,int(mouse[1]/32)-1).mob.hp)
                    #wywolaj funkcje wyswietlajaca informacje o mobie
                   # if maps.get(logika.gracz.mmap).get_tile(int(mouse[0]/32)-1,int(mouse[1]/32)-1).mob.x != logika.gracz.x and maps.get(logika.gracz.mmap).get_tile(int(mouse[0]/32)-1,int(mouse[1]/32)-1).mob.y != logika.gracz.y:
                    #    app.mob_pane = True
                    #else:
                    #    app.mob_pane = False
            elif event.button == 3:
                '''right mouse button'''
                pass