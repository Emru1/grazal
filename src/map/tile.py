class Tile:

    def __init__(self):
        self.passable = bool
        self.transparent = bool
        self.light = int
        self.asset = str
        self.furn = str
        self.mob = {}
        self.obj = {}
        self.area = {}

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

    def initd(self, token):
        self.passable = token['passable']
        self.asset = token['asset']
        self.furn = token['furn']
        self.light = token['light']
        self.transparent = token['transparent']
        self.mob = token['mob']
        self.obj = token['obj']
        self.area = token['area']
