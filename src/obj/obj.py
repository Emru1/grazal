# TO DO:
# podzial na przedmioty (to trzeba zrobic dobrze), gotowe klasy
# podnoszenie/upuszczanie przedmiotow
# rysowanie

import pygame


class Object:
    def __init__(self, pos_x, pos_y, image, taken, visible, window):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(image)
        self.taken = taken
        self.visible = visible

        self.draw(window)

    def draw(self,win):
        if self.visible:
            win.blit(self.image, (self.pos_x, self.pos_y))
            pygame.display.update()

## do testow!!!


pygame.init()
win = pygame.display.set_mode((800,600))
bg = pygame.image.load('volvo.jpg')
bg = pygame.transform.scale(bg,(800,600))
win.blit(bg,(0,0))
pygame.display.update()

obj2 = Object(189,1,"sword.png",True,True,win)


run = True
while run:
    pygame.time.delay(50)
    #win.blit(obj,(0,156))
    #pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False














