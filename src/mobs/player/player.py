from src.globals import maps
from src.mobs.mob import Mob


class Player(Mob):
    def __init__(self, x, y, mmap, hp, attack, movement, sprite):
        super().__init__(x, y, mmap, hp, attack, movement, sprite, name="Player")
        self.near_player = True
        self.eq = []
        self.eq_max = 20
        self.eq_count = 0
        self.weapon = None
        self.armor = None
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0

    def moveup(self):
        if maps.get(self.mmap).get_tile(self.x, self.y - self.movement).passable:
            if not maps.get(self.mmap).get_tile(self.x, self.y - self.movement).mob:
                if self.up == 0 or self.up % 3 == 0:
                    self.up = self.up + 1
                    self.asset = "gora"
                elif self.up % 3 == 1:
                    self.up = self.up + 1
                    self.asset = "gora2"
                elif self.up % 3 == 2:
                    self.up = self.up + 1
                    self.asset = "gora3"
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.y = self.y - self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def movedown(self):
        if maps.get(self.mmap).get_tile(self.x, self.y + self.movement).passable:
            if not maps.get(self.mmap).get_tile(self.x, self.y + self.movement).mob:
                if self.down == 0 or self.down % 3 == 0:
                    self.down = self.down + 1
                    self.asset = "ludek"
                elif self.down % 3 == 1:
                    self.down = self.down + 1
                    self.asset = "ludek2"
                elif self.down % 3 == 2:
                    self.down = self.down + 1
                    self.asset = "ludek3"
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.y = self.y + self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def moveleft(self):
        if maps.get(self.mmap).get_tile(self.x - self.movement, self.y).passable:
            if not maps.get(self.mmap).get_tile(self.x - self.movement, self.y).mob:
                if self.left == 0 or self.left % 3 == 0:
                    self.left = self.left + 1
                    self.asset = "lewo"
                elif self.left % 3 == 1:
                    self.left = self.left + 1
                    self.asset = "lewo2"
                elif self.left % 3 == 2:
                    self.left = self.left + 1
                    self.asset = "lewo3"
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.x = self.x - self.movement
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def moveright(self):
        if maps.get(self.mmap).get_tile(self.x + self.movement, self.y).passable:
            if not maps.get(self.mmap).get_tile(self.x + self.movement, self.y).mob:
                if self.right == 0 or self.right % 3 == 0:
                    self.right = self.right + 1
                    self.asset = "prawo"
                elif self.right % 3 == 1:
                    self.right = self.right + 1
                    self.asset = "prawo2"
                elif self.right % 3 == 2:
                    self.right = self.right + 1
                    self.asset = "prawo3"
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
