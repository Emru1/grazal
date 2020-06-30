from src.globals import maps

class Mob:
    """
    uniwersalna klasa symbolizująca generycznego moba
    może to być postać gracza, przeciwnik lub NPC
    """
    def __init__(self, x, y, mmap, asset=None):
        self.x = x
        self.y = y
        self.move_queue = []
        self.mmap = mmap
        if not asset:
            self.asset = "ludek"
        else:
            self.asset = asset

    def pos(self):
        """
        zwraca krotke z pozycja moba
        :return: (x, y)
        """
        return self.x, self.y

    def calculate_path(self, x, y):
        curr = (self.x, self.y)
        dest = (x, y)
        visited = set()
        dist = 0
        to_check = [curr]
        while True:
            curr = to_check[0]
            to_check.pop(0)



class Enemy(Mob):
    def __init__(self, x, y, asset):
        super().__init__(x, y, asset)

