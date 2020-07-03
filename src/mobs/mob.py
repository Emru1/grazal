from src.globals import maps



class Mob:
    """
    uniwersalna klasa symbolizująca generycznego moba
    może to być postać gracza, przeciwnik lub NPC
    """
    def __init__(self, x, y, mmap, hp, attack, movement, asset=None):
        self.x = x
        self.y = y
        self.move_queue = []
        self.hp = hp
        self.attack = attack
        self.movement = movement
        self.mmap = mmap
        if not asset:
            self.asset = "ludek"
        else:
            self.asset = asset

        maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def pos(self):
        """
        zwraca krotke z pozycja moba
        :return: (x, y)
        """
        return self.x, self.y

    '''def calculate_path(self, x, y):
        class DijkstraStruct:
            def __init__(self, pos, dist):
                self.pos = pos
                self.dist = dist

        curr = (self.x, self.y)
        dest = (x, y)
        visited = set()
        dist = 0
        to_check = [curr]
        while True:
            curr = to_check[0]
            to_check.pop(0)'''


class Enemy(Mob):
    def __init__(self, x, y, asset):
        super().__init__(x, y, asset)
