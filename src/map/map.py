from map.tile import Tile
from globals import log
import string


class Map:

    def token_to_tile(self, token):
        tile = []
        token_list = token.split('; ')
        if token_list[0] == '0':
            tile.append(False)
        else:
            tile.append(True)
        for i in range(1, len(token_list)):
            tile.append(token_list[i])
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
                pass
                #tu będzie zapisywanie mapy

