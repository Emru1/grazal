class Object:
    def __init__(self, pos_x, pos_y, asset):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.asset = asset
        self.can_eq = False
        self.can_mv = False
        self.on_ground = True


class Weapon(Object):
    def __init__(self, pos_x, pos_y, asset, attack):
        super().__init__(pos_x, pos_y, asset)
        self.weapon = True
        self.attack_val = attack


class Armor(Object):
    def __init__(self, pos_x, pos_y, asset, armor):
        super().__init__(pos_x, pos_y, asset)
        self.armor = True
        self.armor = armor


class Edible(Object):
    def __init__(self, pos_x, pos_y, asset):
        super().__init__(pos_x, pos_y, asset)
        self.edible = True


class Potion(Edible):
    def __init__(self, pos_x, pos_y, asset, hp_or_mp, points):
        super().__init__(pos_x, pos_y, asset)
        self.hp_or_mp = hp_or_mp
        self.points = points

    def use(self, mob):
        if self.hp_or_mp:
            if mob.hp_max > self.points + mob.hp:
                mob.hp = mob.hp_max
            else:
                mob.hp = mob.hp + self.points
