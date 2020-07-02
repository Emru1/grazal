from src.mobs.mob import Mob


class Player(Mob):

    def __init__(self,x,y,mmap,hp,attack,movement,sprite):
        super().__init__(x,y,mmap,hp,attack,movement,sprite)
        self.eq = []

    def show(self):
        showSprite(self.sprite)


    def move(self, x, y):
        moveSprite(self.sprite, x, y)

    def moveup(self,mapa):
        #if mapa.get_tile(self.x,self.y+self.movement).passable:
        self.y = self.y-self.movement

         


    def pick_item(self, item):
        self.eq.append(item)

    def drop_item(self):
        pass

    def attack(self, mob):
        pass
