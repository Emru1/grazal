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

    def moveup(self):
        self.move_to(self.x, self.y - 1)

    def movedown(self):
        self.move_to(self.x, self.y + 1)

    def moveleft(self):
        self.move_to(self.x - 1, self.y)

    def moveright(self):
        self.move_to(self.x + 1, self.y)

    def pick_item(self, item):
        self.eq.append(item)
        self.eq_count = self.eq_count + 1

    def drop_item(self):
        pass

    def able_to_attack(self, mob):
        if (self.x + 1, self.y) == mob.pos() or (self.x - 1, self.y) == mob.pos() or (
                self.x, self.y + 1) == mob.pos() or (self.x, self.y - 1) == mob.pos():
            return True
        else:
            return False

    def interaction_attack(self, mob, logika):
        if mob:
            if self.able_to_attack(mob):
                if mob.hp - self.attack <= 0:
                    mob.lethal(logika)
                else:
                    mob.hp = mob.hp - self.attack

    def interaction_pickup(self, item, logika):
        if item:
            if self.able_to_attack(item):
                self.pick_item(item)
                maps.get(self.mmap).get_tile(item.pos()[0], item.pos()[1]).obj = None
