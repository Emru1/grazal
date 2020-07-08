from src.mobs.mob import Mob, Enemy
from src.obj.obj import *


class Tile:

    def __init__(self):
        self.ipassable = bool
        self.transparent = bool
        self.light = int
        self.asset = str
        self.furn = str
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
        self.asset = token['asset']
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
