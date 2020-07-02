from src.mobs.mob import Mob
from src.globals import maps


class Player(Mob):

    def __init__(self,x,y,mmap,hp,attack,movement,sprite):
        super().__init__(x,y,mmap,hp,attack,movement,sprite)
        self.eq = []

    def show(self):
        showSprite(self.sprite)


    def move(self, x, y):
        moveSprite(self.sprite, x, y)

    def moveup(self):
        if maps.get(self.mmap).get_tile(self.x,self.y-self.movement).passable:
            if not maps.get(self.mmap).get_tile(self.x, self.y - self.movement).mob:
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.y = self.y-self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def movedown(self):
        if maps.get(self.mmap).get_tile(self.x,self.y+self.movement).passable:
            if not maps.get(self.mmap).get_tile(self.x, self.y + self.movement).mob:
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.y = self.y+self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def moveleft(self):
        if maps.get(self.mmap).get_tile(self.x-self.movement,self.y).passable:
            if not maps.get(self.mmap).get_tile(self.x-self.movement, self.y).mob:
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.x = self.x-self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self
    
    def moveright(self):
        if maps.get(self.mmap).get_tile(self.x+self.movement,self.y).passable:
            if not maps.get(self.mmap).get_tile(self.x+self.movement, self.y).mob:
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.x = self.x+self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self
         


    def pick_item(self, item):
        self.eq.append(item)

    def drop_item(self):
        pass

    def attack(self, mob):
        pass
