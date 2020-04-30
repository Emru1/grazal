from map.tile import Tile

class Map:

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

    2 2
    1
    a b
    d c
    a = [1 grass dog 0]
    b = [0 rock 0 0]
    c = [1 grass 0 bag]
    d = [1 sand 0 bag coin pen]
    """
    def __init__(self, path):
        plik_mapy = open(path, "r")
        size = plik_mapy.readline()
        wymiary = [int(s) for s in size.split() if s.isdigit()]

        self.sizex = wymiary[0]
        self.sizey = wymiary[1]
        self.cell_size = plik_mapy.readline()
        map_array = []
        map_tokens = {}

        for y in range(self.sizey):
            liney = plik_mapy.readline().rstrip('\n').split(" ", self.sizex - 1)
            map_array.append(liney)

        '''for y in range(self.sizey):
            print(y, end=' ')
            for x in range(self.sizex):
                print(map_array[x][y], end=' ')
            print("\n")'''




    def token_to_tile(self, token):


        return tile

