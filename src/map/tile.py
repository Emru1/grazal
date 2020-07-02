from src.mobs.mob import Mob


class Tile:

    def __init__(self):
        self.passable = bool
        self.transparent = bool
        self.light = int
        self.asset = str
        self.furn = str
        self.mob = None
        self.obj = {}
        self.area = {}
        self.tmob = {}

    def init(self, token):
        self.passable = token.passable
        self.asset = token.asset
        self.furn = token.furn
        self.light = token.light
        self.transparent = token.transparent
        if token.mob != '0':
            self.mob = token.mob
        self.obj = token.obj
        return self

    def initd(self, token, x, y, path):
        self.passable = token['passable']
        self.asset = token['asset']
        self.furn = token['furn']
        self.light = token['light']
        self.transparent = token['transparent']
        if token['mob']:
            self.tmob = token['mob']
        self.obj = token['obj']
        self.area = token['area']

    def addmob(self, x, y, path):
        if self.tmob:
            self.mob = Mob(x, y, path, 100, 1, 1, self.tmob['asset'].rstrip('\n'))
