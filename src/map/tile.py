from src.mobs.mob import Mob, Enemy


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
        if token['passable'] == '0':
            self.passable = False
        else:
            self.passable = True
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
            name = ''
            if 'name' in self.tmob:
                name = self.tmob['name']
            if 'type' in self.tmob:
                if self.tmob['type'] == 'enemy':
                    self.mob = Enemy(x, y, path, 40, 10, 1, self.tmob['asset'], name)
                else:
                    self.mob = Mob(x, y, path, 100, 1, 1, self.tmob['asset'], name)
            else:
                self.mob = Mob(x, y, path, 100, 1, 1, self.tmob['asset'], name)
