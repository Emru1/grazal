

class Tile:

    def __init__(self):
        self.passable = bool
        self.tile = str
        self.obj = str
        self.mob = str
        self.item = []

    def init(self, token):
        self.passable = token.passable
        self.tile = token.asset
        self.obj = token.obj
        if token.mob != '0':
            self.mob = token.mob
        for it in token.items:
            self.item.append(it)
