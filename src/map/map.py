"""
Wczytywanie mapy z lokalizacji path
pierwsze linia to wymiary mapy X x Y
druga linia to dlugosc pojedynczego tokenu czy może symbolu
kolejne Y linii to kolejne tokeny ktore symbolizują kolejne kafelki
pod tym jest rozwinięcie tokenów w klamerkach, ich parametry oraz dodatkowe atrybuty
każdy kafelek może miec dodatkowe obiekty, takie jak itemy czy moby
przedmioty(obj), moby(mob), area(area) itp
każde z nich ma swoje rozwiniecie w klamerkach, ktore jest przekazywane do konstruktora
odpowiedniej klasy jako słownik <parametr, wartosc>
"""

from src.globals import log
from src.map.tile import Tile


class Token:

    def __init__(self, passable, transparent, area, asset, furn, mob, obj, light):
        self.passable = passable
        self.transparent = transparent
        self.area = area
        self.asset = asset
        self.furn = furn
        self.mob = mob
        self.obj = obj
        self.light = light


class Map:
    empty_token = Token(0, 0, 'OUT', 'black', '', '', [], 16)
    empty_tile = Tile()
    empty_tile.init(empty_token)

    @staticmethod
    def parse_tokens(file, file_pos, line_num):
        return_dict = {}
        tmp_dict = {}

        token = ""
        val = False

        in_token = False
        in_obj = False
        in_mob = False
        in_area = False

        file.seek(file_pos)
        for line in file:
            line_num += 1
            line = line.splitlines()[0]
            line = line.lstrip(' ')
            if line[0] == '#':
                continue
            if line[0] == '{':
                if in_token:
                    log.log("Error when parsing map file " + file.name + " at line " + str(line_num))
                    break
                else:
                    in_token = True
                    tmp_dict['passable'] = True
                    tmp_dict['asset'] = ""
                    tmp_dict['asset2'] = ""
                    tmp_dict['furn'] = ""
                    tmp_dict['light'] = 0
                    tmp_dict['transparent'] = 1
                    tmp_dict['mob'] = {}
                    tmp_dict['obj'] = {}
                    tmp_dict['area'] = {}

                    continue
            if not in_token:
                line.rstrip()
                token = line
                token.rstrip()
                continue
            if line[0] == '}':
                in_token = False
                return_dict[token] = tmp_dict
                tmp_dict = {}
                continue

            param = line.split(' ')[0]
            if len(line.split(' ')) > 1:
                val = line.split(' ')[1]
            if in_token:
                if param == 'transparent':
                    tmp_dict[param] = bool(val)
                    continue
                if param == 'passable':
                    tmp_dict[param] = val
                    continue
                if param == 'light':
                    tmp_dict[param] = int(val)
                    continue
                if param == 'asset':
                    tmp_dict[param] = val
                    continue
                if param == 'asset2':
                    tmp_dict[param] = val
                    continue

                if param == 'mob':
                    for line_mob in file:
                        line_mob = line_mob.lstrip(' ')
                        line_num += 1
                        if line_mob[0] == '#':
                            continue
                        if line_mob[0] == '{':
                            if in_mob:
                                log.log("MAP: Error when parsing map file " + file.name + " at line " + str(line_num))
                            tmp_dict['mob'] = {}
                            in_mob = True
                            continue
                        if line_mob[0] == '}':
                            in_mob = False
                            break
                        line_mob_param = line_mob.split(' ')[0]
                        line_mob_val = line_mob.split(' ')[1].rstrip('\n')
                        tmp_dict['mob'][line_mob_param] = line_mob_val

                if param == 'obj':
                    for line_obj in file:
                        line_obj = line_obj.lstrip(' ')
                        line_num += 1
                        if line_obj[0] == '#':
                            continue
                        if line_obj[0] == '{':
                            if in_obj:
                                log.log("MAP: Error when parsing map file " + file.name + " at line " + str(line_num))
                            tmp_dict['obj'] = {}
                            in_obj = True
                            continue
                        if line_obj[0] == '}':
                            in_obj = False
                            break
                        line_obj_param = line_obj.split(' ')[0]
                        line_obj_val = line_obj.split(' ')[1].rstrip('\n')
                        tmp_dict['obj'][line_obj_param] = line_obj_val
        return return_dict

    def __init__(self, path):
        line_num = 0
        self.path = path
        self.name = ''
        plik_mapy = open("maps/" + self.path, "r")
        log.log("File " + path + " opened to read map")
        size = plik_mapy.readline()
        line_num += 1
        wymiary = [int(s) for s in size.split() if s.isdigit()]

        self.sizex = wymiary[0]
        self.sizey = wymiary[1]
        self.cell_size = int(plik_mapy.readline())
        self.map = [[Tile() for x in range(self.sizex)] for y in range(self.sizey)]
        line_num += 1
        self.map_array = []

        for y in range(self.sizey):
            liney = plik_mapy.readline().rstrip('\n').split(" ", self.sizex - 1)
            line_num += 1
            self.map_array.append(liney)

        self.map_tokens = self.parse_tokens(plik_mapy, plik_mapy.tell(), line_num)
        plik_mapy.close()

        for y in range(self.sizey):
            for x in range(self.sizex):
                self.map[x][y].initd(self.map_tokens[self.map_array[y][x]], x, y, self.path)

    def initmobs(self):
        for y in range(self.sizey):
            for x in range(self.sizex):
                self.map[x][y].addmob(x, y, self.path)

    def get_tile(self, x, y):
        if x < 0 or x > self.sizex - 1 or y < 0 or y > self.sizey - 1:
            return self.empty_tile
        return self.map[x][y]

    def putobj(self, obj):
        x = obj.pos_x
        y = obj.pos_y
        dd = 0
        while True:
            tile = self.get_tile(x, y)
            if tile.obj or not tile.ipassable:
                dd = dd + 1
                dd = dd % 4
            else:
                obj.pos_y = y
                obj.pos_x = x
                tile.obj = obj
                break
            if dd == 0:
                x = x + 1
            elif dd == 1:
                y = y + 1
            elif dd == 2:
                x = x - 1
            elif dd == 3:
                y = y - 1
