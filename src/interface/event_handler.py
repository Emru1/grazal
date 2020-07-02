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
                pass
            elif event.key == pygame.K_s:
                '''move down'''
                pass
            elif event.key == pygame.K_a:
                '''move left'''
                pass
            elif event.key == pygame.K_d:
                '''move right'''
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                '''Left mouse button'''
                pass
            elif event.button == 3:
                '''right mouse button'''
                pass