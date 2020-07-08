class Object:
    def __init__(self, pos_x, pos_y, path, asset, name, description):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.asset = asset
        self.mmap = path
        self.can_eq = False
        self.can_mv = False
        self.on_ground = True
        self.passable = True
        self.edible = False
        self.weapon = False
        self.armor = False
        self.name = name
        self.description = description

    def pos(self):
        return self.pos_x, self.pos_y


class Weapon(Object):
    def __init__(self, pos_x, pos_y, path, asset, name, description, attack):
        super().__init__(pos_x, pos_y, path, asset, description, name)
        self.attack_val = attack
        self.can_eq = True
        self.can_mv = True
        self.weapon = True

    def equip(self, mob):
        if not mob.weapon:
            mob.weapon = self
            mob.attack = mob.attack + self.attack_val
            return False
        else:
            # zamien itemki
            return True

    def unequip(self, mob):
        if mob.weapon != None:
            mob.attack = mob.attack - self.attack_val
            mob.weapon = None



class Armor(Object):
    def __init__(self, pos_x, pos_y, path, asset, name , description, armor_val):
        super().__init__(pos_x, pos_y, path, asset, name)
        self.armor = True
        self.armor_val = armor_val
        self.can_eq = True
        self.can_mv = True

    def equip(self, mob):
        if not mob.armor:
            mob.armor = self
            mob.armor_val = mob.armor_val + self.armor_val
            return False
        else:
            # zamien itemki
            return True
    def unequip(self, mob):
        mob.armor_val = mob.armor_val - self.armor_val
        mob.armor = None


class Edible(Object):
    def __init__(self, pos_x, pos_y, path, asset, name, description):
        super().__init__(pos_x, pos_y, path, asset, name, description)
        self.can_eq = True
        self.can_mv = True
        self.edible = True

    def use(self, mob):
        pass


class Potion(Edible):
    def __init__(self, pos_x, pos_y, path, asset, name, description, hp_or_mp, points):
        super().__init__(pos_x, pos_y, path, asset, description, name)
        self.hp_or_mp = hp_or_mp
        self.points = points

    def use(self, mob):
        if self.hp_or_mp:
            if mob.hp_max < self.points + mob.hp:
                mob.hp = mob.hp_max
            else:
                mob.hp = mob.hp + self.points
