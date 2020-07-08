class Object:
    def __init__(self, pos_x, pos_y, path, asset):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.asset = asset
        self.mmap = path
        self.can_eq = False
        self.can_mv = False
        self.on_ground = True
        self.passable = True

    def pos(self):
        return self.pos_x, self.pos_y


class Weapon(Object):
    def __init__(self, pos_x, pos_y, path, asset, attack):
        super().__init__(pos_x, pos_y, path, asset)
        self.attack_val = attack
        self.can_eq = True
        self.can_mv = True


class Armor(Object):
    def __init__(self, pos_x, pos_y, path, asset, armor):
        super().__init__(pos_x, pos_y, path, asset)
        self.armor = armor
        self.can_eq = True
        self.can_mv = True


class Edible(Object):
    def __init__(self, pos_x, pos_y, path, asset):
        super().__init__(pos_x, pos_y, path, asset)
        self.can_eq = True
        self.can_mv = True


class Potion(Edible):
    def __init__(self, pos_x, pos_y, path, asset, hp_or_mp, points):
        super().__init__(pos_x, pos_y, path, asset)
        self.hp_or_mp = hp_or_mp
        self.points = points

    def use(self, mob):
        if self.hp_or_mp:
            if mob.hp_max > self.points + mob.hp:
                mob.hp = mob.hp_max
            else:
                mob.hp = mob.hp + self.points
