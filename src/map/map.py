from map.tile import Tile
from globals import log
import string


class Token:

    def __init__(self, passable, asset, obj, mob, items):
        self.passable = passable
        self.asset = asset
        self.obj = obj
        self.mob = mob
        self.items = items


class Map:

    def token_to_tile(self, token):
        token_list = token.split('; ')
        if token_list[0] == '':
            return
        passable = bool(token_list[0])  # passable
        asset = str(token_list[1])      # asset
        obj = str(token_list[2])
        mob = str(token_list[3])        # mob
        items = []
        for x in range(4, len(token_list)):
            items.append(token_list[x])
        tile = Token(passable, asset, obj, mob, items)
        return tile

    """
    Wczytywanie mapy z lokalizacji path
    pierwsze linia to wymiary mapy X x Y
    druga linia to dlugosc pojedynczego tokenu czy może symbolu
    kolejne Y linii to kolejne tokeny które symbolizują kolejne kafelki
    pod tym jest rozwinięcie tokenów, co one oznaczają
    kolejnosc: passable, asset, mob, item(s)
    passable - czy mozna przejsc, 0, 1
    asset - nazwa grafiki, string
    obj - obiekty, string
    mob - spawn point moba, string
    item(s) - lista przedmiotow, string
    """
    def __init__(self, path):
        plik_mapy = open(path, "r")
        log.log("File " + path + " opened to read map")
        size = plik_mapy.readline()
        wymiary = [int(s) for s in size.split() if s.isdigit()]

        self.sizex = wymiary[0]
        self.sizey = wymiary[1]
        self.cell_size = int(plik_mapy.readline())
        self.map = [[Tile() for x in range(self.sizex)] for y in range(self.sizey)]
        map_array = []
        map_tokens = {}

        for y in range(self.sizey):
            liney = plik_mapy.readline().rstrip('\n').split(" ", self.sizex - 1)
            map_array.append(liney)

        for line in plik_mapy:
            token = line[:self.cell_size]
            line = line[3+self.cell_size:]
            line = line.rstrip('\n')
            map_tokens[token] = self.token_to_tile(line)

        for y in range(self.sizey):
            for x in range(self.sizex):
                self.map[x][y].init(token=map_tokens[map_array[x][y]])

    def get_tile(self, x, y):
        return self.map[x][y]


