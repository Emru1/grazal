import random

from src.obj.obj import Potion, Weapon, Armor
from src.globals import maps, objs


class Mob:
    """
    uniwersalna klasa symbolizująca generycznego moba
    może to być postać gracza, przeciwnik lub NPC
    """

    def __init__(self, x, y, mmap, hp, attack, movement, asset=None, name=None, drop=[]):
        self.x = x
        random.seed()
        self.y = y
        self.move_queue = []
        self.hp = hp
        self.hp_max = hp
        self.hp_last = hp
        self.attack = attack
        self.movement = movement
        self.armor_val = 0
        self.mmap = mmap
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.drop = drop
        '''self.dropable = [
            (Potion(self.x, self.y, self.mmap, 'potions0', 'Mikstura życia', 'Leczy gracza o 20 hp', 1, 20), 70),
            (Weapon(self.x, self.y, self.mmap, 'Miecz', 'Srebrny Miecz', 'Zwieksza sile ataku o 10', 10), 80),
            (Weapon(self.x, self.y, self.mmap, 'Czarny_miecz', 'Miecz czarnej skały', 'Zwieksza sile ataku o 20', 20),
             50),
            (Weapon(self.x, self.y, self.mmap, 'Zloty_miecz', 'Zloty Miecz', 'Zwieksza sile ataku o 30', 30), 40),
            (
            Weapon(self.x, self.y, self.mmap, 'Czarny_kos', 'Miecz Czarnego Kosa', 'Zwieksza sile ataku o 40', 40), 30),
            (Weapon(self.x, self.y, self.mmap, 'Szabelka', 'Krótka Szabla', 'Zwieksza sile ataku o 15', 15), 80),
            (Weapon(self.x, self.y, self.mmap, 'Dluga_szabla', 'Długa Szabla', 'Zwieksza sile ataku o 25', 25), 70),
            (Weapon(self.x, self.y, self.mmap, 'Siekiera', 'Siekiera', 'Zwieksza sile ataku o 35', 35), 60),
            (Weapon(self.x, self.y, self.mmap, 'Mjolnir', 'StormBreaker', 'Zwieksza sile ataku o 50', 50), 80),
            (Armor(self.x, self.y, self.mmap, 'Zbroja_miedz', 'Miedziana Zbroja', 'Zwieksza obrone gracza o 10', 10),
             50),
            (Armor(self.x, self.y, self.mmap, 'Zbroja_diament', 'Diamentowa Zbroja', 'Zwieksza obrone gracza o 30', 30),
             30),
            (Armor(self.x, self.y, self.mmap, 'Zbroja_jungla', 'Leśna Zbroja', 'Zwieksza obrone gracza o 5', 5), 80),
            (Armor(self.x, self.y, self.mmap, 'Zbroja_smoka', 'Smocza Zbroja', 'Zwieksza obrone gracza o 40', 40), 20)]'''

        if not asset:
            self.asset = "ludek"
        else:
            self.asset = asset
        self.asset_base = self.asset

        if not name:
            self.name = "Mob"
        else:
            self.name = name

        maps.get(self.mmap).get_tile(self.x, self.y).mob = self


    def lethal(self, logika):
        self.hp = 0
        maps.get(self.mmap).get_tile(self.x, self.y).mob = None
        # losuj item
        obj = random.choice(self.drop)
        number = random.randint(0, 100)
        if number <= int(obj[1]):
            maps.get(self.mmap).putobj(objs.get_item(self.x, self.y, self.mmap, obj[0]))
        logika.wrogowie.remove(self)
        del self

    def pos(self):
        """
        zwraca krotke z pozycja moba
        :return: (x, y)
        """
        return self.x, self.y

    def find_path(self, dest_x, dest_y):
        """
        :param: współrzędne gracza, do którego szukamy najkrótszej ścieżki
        :return: lista z najkrótszą ścieżką!
        """

        def __get_neigh(x, y):
            ret = []
            tile = maps.get(self.mmap).get_tile(x - 1, y)
            if tile.ispassable():
                ret.append((x - 1, y))
            tile = maps.get(self.mmap).get_tile(x + 1, y)
            if tile.ispassable():
                ret.append((x + 1, y))
            tile = maps.get(self.mmap).get_tile(x, y - 1)
            if tile.ispassable():
                ret.append((x, y - 1))
            tile = maps.get(self.mmap).get_tile(x, y + 1)
            if tile.ispassable():
                ret.append((x, y + 1))
            return ret

        def __return_coord(vert):
            ret = vert
            while True:
                ret = parents[ret]
                if ret == self.pos() or parents[ret] == self.pos():
                    return ret

        if abs(dest_x - self.x) > 20 or abs(dest_x - self.y) > 20:
            return None
        lista = [self.pos()]
        visited = set()
        parents = {}

        while lista:
            vertex = lista.pop(0)
            if vertex[0] == dest_x and vertex[1] == dest_y:
                return __return_coord(vertex)
            visited.add(vertex)
            neigs = __get_neigh(vertex[0], vertex[1])
            for neig in neigs:
                if neig not in visited and neig not in lista:
                    lista.append(neig)
                    parents[neig] = vertex
        return None

    def move_to(self, dest_x, dest_y):
        if maps.get(self.mmap).get_tile(dest_x, dest_y).ispassable():
            if dest_x < self.x:
                self.asset = self.asset_base + "lewo"
                self.left = self.left % 3
                self.left = self.left + 1
                self.asset = self.asset + str(self.left)
            elif dest_x > self.x:
                self.asset = self.asset_base + "prawo"
                self.right = self.right % 3
                self.right = self.right + 1
                self.asset = self.asset + str(self.right)
            elif dest_y < self.y:
                self.asset = self.asset_base + "gora"
                self.up = self.up % 3
                self.up = self.up + 1
                self.asset = self.asset + str(self.up)
            elif dest_y > self.y:
                self.asset = self.asset_base + "dol"
                self.down = self.down % 3
                self.down = self.down + 1
                self.asset = self.asset + str(self.down)
            maps.get(self.mmap).get_tile(self.x, self.y).mob = None
            self.y = dest_y
            self.x = dest_x
            maps.get(self.mmap).get_tile(self.x, self.y).mob = self


class Enemy(Mob):
    def __init__(self, x, y, mmap, hp, attack, movement, asset=None, name=None, drop=[]):
        super().__init__(x, y, mmap, hp, attack, movement, asset, name, drop)
        self.agressive = False
        self.attacked = False
        self.able_to_attack = False

    def check_range(self, player):
        if self.pos() == (player.x - 1, player.y) or self.pos() == (player.x + 1, player.y) or self.pos() == (
                player.x, player.y - 1) or self.pos() == (player.x, player.y + 1):
            return True

    def action(self, player):
        # calculate damage reduction
        if player.armor_val > 0:
            if self.attack - player.armor_val <= 0:
                player.hp = player.hp - 1
            else:
                player.hp = player.hp - (self.attack - player.armor_val)
        else:
            player.hp = player.hp - self.attack
