class com_Creature:

    def __init__(self, name, attack=2, deff=0, hp=10, dict={}):
        self.name_instance = name
        self.base_atk = attack
        self.base_def = deff
        self.max_hp = hp
        self.current_hp = hp
        self.dict = dict

    def move(self, dx, dy):
        if target:
            self.attack(target)  # bije na dziure playera

        if target is None:
            self.owner.x += dx
            self.owner.y += dy

    def attack(self, target):
        damage_dealt = self.power - target.creature.defense
        print(self.name_instance + " atakuje " + target.creature.name_instance + " zadajac " + str(
            damage_dealt) + " obrazen!")
        target.creature.take_damage(damage_dealt)

    def take_damage(self, damage):
        self.current_hp -= damage
        print(self.name_instance + "'s health is " + str(self.current_hp) + "/" + str(self.max_hp))
        if self.current_hp <= 0:
            pass
            # mobek zdycha

    def heal(self, value):
        self.current_hp += value
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
