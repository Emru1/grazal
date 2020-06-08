class Tile:

    def __init__(self):
        self.passable = bool
        self.transparent = bool
        self.light = int
        self.asset = str
        self.furn = str
        self.mob = str
        self.obj = []

    def init(self, token):
        self.passable = token.passable
        self.asset = token.asset
        self.furn = token.furn
        self.light = token.light
        self.transparent = token.transparent
        if token.mob != '0':
            self.mob = token.mob
        for it in token.obj:
            self.obj.append(it)
        return self

    def initd(self, token):
        self.passable = token['passable']
        self.asset = token['asset']
        self.furn = token['furn']
        self.light = token['light']
        self.transparent = token['transparent']
        self.mob = token['mob']
        self.obj = token['obj']