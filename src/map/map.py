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

from src.map.tile import Tile
from src.globals import log
import string

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
    empty_token = Token(0, 0, 'OUT', 'out', '', '', [], 16)
    empty_tile = Tile()
    empty_tile.init(empty_token)

    @staticmethod
    def parse_tokens(file, file_pos, line_num):
        return_dict = {}
        tmp_dict = {}

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
                    tmp_dict['passable'] = 1
                    tmp_dict['asset'] = ""
                    tmp_dict['furn'] = ""
                    tmp_dict['light'] = 0
                    tmp_dict['transparent'] = 1
                    tmp_dict['mob'] = ""
                    tmp_dict['obj'] = ""
                    tmp_dict['area'] = ""

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
                if param == 'light':
                    tmp_dict[param] = int(val)
                    continue
                if param == 'asset':
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
                            tmp_dict['mob'] = ""
                            in_mob = True
                            continue
                        if line_mob[0] == '}':
                            in_mob = False
                            break
                        tmp_dict['mob'] += line_area

                if param == 'area':
                    for line_area in file:
                        line_area = line_area.lstrip(' ')
                        line_num += 1
                        if line_area[0] == '#':
                            continue
                        if line_area[0] == '{':
                            if in_area:
                                log.log("MAP: Error when parsing map file " + file.name + " at line " + str(line_num))
                            tmp_dict['area'] = ""
                            in_obj = True
                            continue
                        if line_area[0] == '}':
                            in_area = False
                            break
                        tmp_dict['area'] += line_area

                if param == 'obj':
                    for line_obj in file:
                        line_obj = line_obj.lstrip(' ')
                        line_num += 1
                        if line_obj[0] == '#':
                            continue
                        if line_obj[0] == '{':
                            if in_obj:
                                log.log("MAP: Error when parsing map file " + file.name + " at line " + str(line_num))
                            tmp_dict['obj'] = ""
                            in_obj = True
                            continue
                        if line_obj[0] == '}':
                            in_obj = False
                            break
                        tmp_dict['obj'] += line_obj
        return return_dict


    def __init__(self, path):
        line_num = 0
        plik_mapy = open(path, "r")
        log.log("File " + path + " opened to read map")
        size = plik_mapy.readline()
        line_num += 1
        wymiary = [int(s) for s in size.split() if s.isdigit()]

        self.sizex = wymiary[0]
        self.sizey = wymiary[1]
        self.cell_size = int(plik_mapy.readline())
        self.map = [[Tile() for x in range(self.sizex)] for y in range(self.sizey)]
        line_num += 1
        map_array = []

        for y in range(self.sizey):
            liney = plik_mapy.readline().rstrip('\n').split(" ", self.sizex - 1)
            line_num += 1
            map_array.append(liney)

        map_tokens = self.parse_tokens(plik_mapy, plik_mapy.tell(), line_num)

        for y in range(self.sizey):
            for x in range(self.sizex):
                self.map[x][y].initd(token=map_tokens[map_array[x][y]])

    def get_tile(self, x, y):
        if x < 0 or x > self.sizex or y < 0 or y > self.sizey:
            return self.empty_tile
        return self.map[x][y]


