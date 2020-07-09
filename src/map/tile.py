from src.globals import mobs
from src.obj.obj import *


class Tile:

    def __init__(self):
        self.ipassable = False
        self.asset = ''
        self.asset2 = ''
        self.mob = None
        self.obj = None
        self.area = {}
        self.tmob = {}
        self.tobj = {}

    def init(self, token):
        self.ipassable = token.passable
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
            self.ipassable = False
        else:
            self.ipassable = True
        if token['asset'] == '':
            self.asset = 'test1'
        else:
            self.asset = token['asset']
        self.asset2 = token['asset2']
        self.furn = token['furn']
        self.light = token['light']
        self.transparent = token['transparent']
        if token['mob']:
            self.tmob = token['mob']
        if token['obj']:
            self.tobj = token['obj']
        self.area = token['area']

    def addmob(self, x, y, path):
        if self.tmob:
            self.mob = mobs.get_mob(x, y, path, self.tmob['mob'])

    def addobj(self, x, y, path):
        if self.tobj:
            if 'type' in self.tmob:
                if self.tmob['type'] == 'potion':
                    self.obj = Potion(x, y, path, self.tobj['asset'], 1, 10)
                else:
                    self.obj = Object(x, y, path, self.tobj['asset'])

    def ispassable(self):
        if not self.ipassable:
            return False
        if self.mob:
            if not self.mob.name == 'Player':
                return False
        if self.obj:
            if not self.obj.passable:
                return False
        return True
