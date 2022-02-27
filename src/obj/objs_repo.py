from src.obj.obj import *


class Objs:
    def __init__(self, path):
        self.objs = {}
        file = open(path, 'rt')
        in_token = False
        token = ''
        tmp_dict = {}
        for line in file:
            line = line.splitlines()[0]
            line = line.lstrip(' ')
            if not line:
                continue
            if line[0] == '#':
                continue
            if line[0] == '{':
                if in_token:
                    break
                else:
                    in_token = True
                    tmp_dict['name'] = 'Obj'
                    tmp_dict['obj'] = 'mob'
                    tmp_dict['asset'] = 'potion0'
                    tmp_dict['type'] = 'npc'
                    tmp_dict['desc'] = ''
                    continue

            if not in_token:
                token = line
                token = token.rstrip()
                continue
            if line[0] == '}':
                in_token = False
                self.objs[token] = tmp_dict
                tmp_dict = {}
                continue

            param = line.split(' ')[0]
            if len(line.split(' ')) > 1:
                val = ''
                ltmp = line.split(' ')[1:]
                for x in ltmp:
                    val = val + ' ' + x
                val = val.lstrip(' ')
            else:
                val = ''
            if in_token:
                tmp_dict[param] = val
        file.close()

    def get_item(self, x, y, mmap, name):
        obj = self.objs[name]
        if not obj:
            return None
        if obj['type'] == 'weapon':
            ret = Weapon(x, y, mmap,
                         asset=obj['asset'],
                         name=obj['name'],
                         description=obj['desc'],
                         attack=int(obj['attack']),
                         )
        elif obj['type'] == 'armor':
            ret = Armor(x, y, mmap,
                        asset=obj['asset'],
                        name=obj['name'],
                        description=obj['desc'],
                        armor_val=int(obj['armor_val']),
                        )
        elif obj['type'] == 'potion':
            ret = Potion(x, y, mmap,
                         asset=obj['asset'],
                         name=obj['name'],
                         description=obj['desc'],
                         hp_or_mp=1,
                         points=int(obj['heal']))
        else:
            ret = None
        return ret
