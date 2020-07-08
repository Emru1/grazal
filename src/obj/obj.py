class Object:
    def __init__(self, pos_x, pos_y, asset):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.asset = asset
        self.can_eq = False
        self.can_mv = False
        self.on_ground = True

    def pos(self):
        return (self.pos_x, self.pos_y)


class Weapon(Object):
    def __init__(self, pos_x, pos_y, asset, attack):
        super().__init__(pos_x, pos_y, asset)
        self.weapon = True
        self.attack_val = attack

    def equip(self,mob):
        if mob.weapon == None:
            mob.weapon = self
            mob.attack = mob.attack + self.attack_val


class Armor(Object):
    def __init__(self, pos_x, pos_y, asset, armor_val):
        super().__init__(pos_x, pos_y, asset)
        self.armor = True
        self.armor_val = armor_val

    def equip(self, mob):
        if mob.armor == None:
            mob.armor = self
            mob.armor_val = mob.armor_val+self.armor_val
            return False
        else:
            #zamien itemki
            return True
            


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
            if mob.hp_max < self.points + mob.hp:
                mob.hp = mob.hp_max
            else:
                mob.hp = mob.hp + self.points
