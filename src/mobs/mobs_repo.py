class Mobs:
    def __init__(self, path):
        self.mobs = {}
        file = open(path, 'rt')
        in_token = False
        token = ''
        tmp_dict = {}
        for line in file:
            line = line.splitlines()[0]
            line = line.lstrip(' ')
            if line[0] == '#':
                continue
            if line[0] == '{':
                if in_token:
                    break
                else:
                    in_token = True
                    tmp_dict['name'] = 'Mob'
                    tmp_dict['mob'] = 'mob'
                    tmp_dict['asset'] = 'ss'
                    tmp_dict['attack'] = 10
                    tmp_dict['hp'] = 10
                    tmp_dict['type'] = 'npc'
                    continue

            if not in_token:
                token = line
                token = token.rstrip()
                continue
            if line[0] == '}':
                in_token = False
                self.mobs[token] = tmp_dict
                tmp_dict = {}
                continue

            param = line.split(' ')[0]
            if len(line.split(' ')) > 1:
                val = line.split(' ')[1]
            else:
                val = ''
            if in_token:
                if param == 'mob':
                    tmp_dict[param] = val
                    continue
                if param == 'asset':
                    tmp_dict[param] = val
                    continue
                if param == 'name':
                    tmp_dict[param] = val
                    continue
                if param == 'type':
                    tmp_dict[param] = val
                    continue
                if param == 'attack':
                    tmp_dict[param] = int(val)
                    continue
                if param == 'hp':
                    tmp_dict[param] = int(val)
                    continue
                if param == 'droplist':
                    for line_drop in file:
                        line_drop = line_drop.lstrip(' ').rstrip('\n')
                        print(line_drop)
                        if line_drop[0] == '#':
                            continue
                        if line_drop[0] == '{':
                            tmp_dict['drop'] = {}
                            continue
                        if line_drop[0] == '}':
                            break
                        name = line_drop
                        for line_item in file:
                            line_item = line_item.lstrip(' ').rstrip('\n')
                            if line_item[0] == '#':
                                continue
                            if line_item[0] == '{':
                                tmp_dict['drop'][name] = {}
                                continue
                            if line_item[0] == '}':
                                break
                            item_param = line_item.split(' ')[0]
                            item_val = line_item.split(' ')[1]
                            tmp_dict['drop'][name][item_param] = item_val
        file.close()
        print(self.mobs)


    def get_mob(self, x, y, mmap, name):
        from src.mobs.mob import Mob, Enemy
        mob = self.mobs[name]
        if mob['type'] == 'enemy':
            ret = Enemy(x, y, mmap,
                        hp=mob['hp'],
                        asset=mob['asset'],
                        attack=mob['attack'],
                        name=mob['name'],
                        movement=1
                        )
        else:
            ret = Mob(x, y, mmap,
                      hp=mob['hp'],
                      asset=mob['asset'],
                      attack=mob['attack'],
                      name=mob['name'],
                      movement=1
                      )
        return ret
