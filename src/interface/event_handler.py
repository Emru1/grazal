import pygame

def event_handler(logika,mapa,mobs=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                '''move up'''
                logika.gracz.moveup(mapa)
            elif event.key == pygame.K_s:
                logika.gracz.movedown(mapa)
                '''move down'''
            elif event.key == pygame.K_a:
                logika.gracz.moveleft(mapa)
                '''move left'''
            elif event.key == pygame.K_d:
                logika.gracz.moveright(mapa)
                '''move right'''
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                '''Left mouse button'''
                pass
            elif event.button == 3:
                '''right mouse button'''
                pass