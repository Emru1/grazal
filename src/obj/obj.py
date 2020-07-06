# TO DO:
# drzwi do poprawy
# podzial na przedmioty (to trzeba zrobic dobrze), gotowe klasy
# podnoszenie/upuszczanie przedmiotow
# rysowanie -> w ogólnym interfejsie
# akcje typu otworz/zamknij
# relacje: gracz -> przedmiot

import pygame

static_types = {'chair': "objectsImages/chair.png", 'lamp': "objectsImages/lamp.png",
                'door': "objectsImages/Basic_Door_Pixel.png"}


class Object:
    def __init__(self, pos_x, pos_y, image, taken, visible, window):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(image)
        self.taken = taken
        self.visible = visible
        self.draw(window)

    def draw(self, win, alternative_image=None):
        if self.visible:
            if alternative_image is None:
                win.blit(self.image, (self.pos_x, self.pos_y))
            else:
                win.blit(pygame.image.load(alternative_image), (self.pos_x, self.pos_y))
            pygame.display.update()

    def pick(self, player, win):
        # TO TRZEBA ZROBIC!
        pass


class SwordObject(Object):
    def __init__(self, pos_x, pos_y, window):
        self.volume = 1  # ilość, nie wiem, może się przyda?
        self.damage = 30  # obrażenie zadawane
        self.player_speed = 4  # wpływa na szybkośc poruszania się gracza
        super().__init__(pos_x, pos_y, "objectsImages/sword.png", True, True, window)
        print("STWORZYLES SWOJEGO MIECZA! hehe")


class StaticObject(Object):
    def __init__(self, pos_x, pos_y, type, window):
        self.type = static_types.get(type, 'door')
        super().__init__(pos_x, pos_y, self.type, False, True, window)

    def open_the_door(self, window):
        if self.type == "objectsImages/Basic_Door_Pixel.png":
            self.type = "objectsImages/Basic_Door_Opening_Pixel.png"
            self.draw(window, self.type)

    def close_the_door(self, window):
        if self.type == "objectsImages/Basic_Door_Opening_Pixel.png":
            self.type = "objectsImages/Basic_Door_Pixel.png"
            self.draw(window, self.type)


def create_object(type, pos_x, pos_y, window):
    """przydatne w tworzeniu mapy
    :param typ obiektu, pozycja x, pozycja y, okno
    :return nowy obiekt zgodny z typem
    """
    if type == "SwordObject":
        return SwordObject(pos_x, pos_y, window)
    if type == "door":
        return StaticObject(pos_x, pos_y, "door", window)
    if type == "lamp":
        return StaticObject(pos_x, pos_y, "lamp", window)
    if type == "chair":
        return StaticObject(pos_x, pos_y, "chair", window)

# pygame.init()
# win = pygame.display.set_mode((800, 600))
# bg = pygame.image.load('background.png')
# bg = pygame.transform.scale(bg, (800, 600))
# win.blit(bg, (0, 0))
# pygame.display.update()
#
# sword = create_object("SwordObject", 120, 100, win)
# door = create_object("door", 230, 140, win)
#
# run = True
#    #pygame.time.delay(50)
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            run = False
#        elif event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_w:
#                door.open_the_door(win)
#            if event.key == pygame.K_s:
#                door.close_the_door(win)
