from src.globals import maps
from src.mobs.mob import Mob


class Player(Mob):

    up = 0
    down = 0
    left = 0
    right = 0
    def __init__(self, x, y, mmap, hp, attack, movement, sprite):
        super().__init__(x, y, mmap, hp, attack, movement, sprite, name="Player")
        self.near_player = True
        self.eq = []

    def moveup(self):
        if maps.get(self.mmap).get_tile(self.x, self.y - self.movement).passable:
            if not maps.get(self.mmap).get_tile(self.x, self.y - self.movement).mob:

                self.asset = "gora"
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.y = self.y - self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def movedown(self):
        if maps.get(self.mmap).get_tile(self.x, self.y + self.movement).passable:
            if not maps.get(self.mmap).get_tile(self.x, self.y + self.movement).mob:
                self.asset = "ludek"
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.y = self.y + self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def moveleft(self):
        if maps.get(self.mmap).get_tile(self.x - self.movement, self.y).passable:
            if not maps.get(self.mmap).get_tile(self.x - self.movement, self.y).mob:
                self.asset = "lewo"
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.x = self.x - self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def moveright(self):
        if maps.get(self.mmap).get_tile(self.x + self.movement, self.y).passable:
            if not maps.get(self.mmap).get_tile(self.x + self.movement, self.y).mob:
                self.asset = "prawo"
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.x = self.x + self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def pick_item(self, item):
        self.eq.append(item)

    def drop_item(self):
        pass

    def able_to_attack(self, mob):
        if (self.x + 1, self.y) == mob.pos() or (self.x - 1, self.y) == mob.pos() or (
                self.x, self.y + 1) == mob.pos() or (self.x, self.y - 1) == mob.pos():
            return True
        else:
            return False

    def interaction_attack(self, mob, mouse, logika):
        if mob:
            if self.able_to_attack(mob):
                if mob.hp - self.attack <= 0:
                    mob.lethal(logika)
                else:
                    mob.hp = mob.hp - self.attack
