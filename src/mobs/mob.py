from collections import deque

from src.globals import maps


class Mob:
    """
    uniwersalna klasa symbolizująca generycznego moba
    może to być postać gracza, przeciwnik lub NPC
    """

    def __init__(self, x, y, mmap, hp, attack, movement, asset=None, name=None):
        self.x = x
        self.y = y
        self.move_queue = []
        self.hp = hp
        self.attack = attack
        self.movement = movement
        self.mmap = mmap
        if not asset:
            self.asset = "ludek"
        else:
            self.asset = asset

        if not name:
            self.name = "Mob"
        else:
            self.name = name

        maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    def lethal(self, logika):
        self.hp = 0
        maps.get(self.mmap).get_tile(self.x, self.y).mob = None
        logika.wrogowie.remove(self)
        del self

    def pos(self):
        """
        zwraca krotke z pozycja moba
        :return: (x, y)
        """
        return self.x, self.y

    def find_path(self, dest_x, dest_y):
        """
        :param: współrzędne gracza, do którego szukamy najkrótszej ścieżki
        :return: lista z najkrótszą ścieżką!
        """

        def __get_neigh(x, y):
            ret = []
            tile = maps.get(self.mmap).get_tile(x-1, y)
            if tile.passable:
                if tile.mob:
                    if tile.mob.name == "Player":
                        ret.append((x-1, y))
                else:
                    ret.append((x-1, y))
            tile = maps.get(self.mmap).get_tile(x+1, y)
            if tile.passable:
                if tile.mob:
                    if tile.mob.name == "Player":
                        ret.append((x+1, y))
                else:
                    ret.append((x+1, y))
            tile = maps.get(self.mmap).get_tile(x, y-1)
            if tile.passable:
                if tile.mob:
                    if tile.mob.name == "Player":
                        ret.append((x, y-1))
                else:
                    ret.append((x, y-1))
            tile = maps.get(self.mmap).get_tile(x, y+1)
            if tile.passable:
                if tile.mob:
                    if tile.mob.name == "Player":
                        ret.append((x, y+1))
                else:
                    ret.append((x, y+1))
            return ret

        def __return_coord(vert):
            ret = vert
            while True:
                ret = parents[ret]
                if ret == self.pos() or parents[ret] == self.pos():
                    return ret

        if abs(dest_x - self.x) > 20 or abs(dest_x - self.y) > 20:
            return None
        lista = [self.pos()]
        visited = set()
        parents = {}

        while lista:
            vertex = lista.pop(0)
            if vertex[0] == dest_x and vertex[1] == dest_y:
                return __return_coord(vertex)
            visited.add(vertex)
            neigs = __get_neigh(vertex[0], vertex[1])
            for neig in neigs:
                if neig not in visited and neig not in lista:
                    lista.append(neig)
                    parents[neig] = vertex
        return None


        '''neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        queue.append((self.pos()))
        path = {}
        result_path = deque()
        path[self.pos()] = None

        while len(queue) > 0:
            curr_x, curr_y = queue.popleft()
            if curr_x == dest_x and curr_y == dest_y:
                break
            for neig_x, neig_y in neighbours:
                is_mob = bool(maps.get(self.mmap).get_tile(curr_x + neig_x, curr_y + neig_y).mob)
                is_passable = maps.get(self.mmap).get_tile(curr_x + neig_x, curr_y + neig_y).passable
                if (is_passable or not is_mob) and (curr_x + neig_x, curr_y + neig_y) not in path:
                    queue.append((curr_x + neig_x, curr_y + neig_y))
                    path[(curr_x + neig_x, curr_y + neig_y)] = (curr_x, curr_y)

        result_path.appendleft((dest_x, dest_y))
        curr_vertex = path.get((dest_x, dest_y))
        while curr_vertex and curr_vertex != self.pos():
            curr_vertex = path.get(curr_vertex)
            if curr_vertex:
                result_path.appendleft(curr_vertex)
        if len(result_path) >= 2:
            return result_path[1]
        else:
            return result_path[0]'''

    def move_to(self, dest_x, dest_y):
        if maps.get(self.mmap).get_tile(dest_x, dest_y).passable:
            if not maps.get(self.mmap).get_tile(dest_x, dest_y).mob:
                maps.get(self.mmap).get_tile(self.x, self.y).mob = None
                self.y = dest_y
                self.x = dest_x
                maps.get(self.mmap).get_tile(self.x, self.y).mob = self


class Enemy(Mob):
    def __init__(self, x, y, mmap, hp, attack, movement, asset=None, name=None):
        super().__init__(x, y, mmap, hp, attack, movement, asset, name)
        self.agressive = False
        self.attacked = False
        self.able_to_attack = False

    def check_range(self, player):
        if self.pos() == (player.x - 1, player.y) or self.pos() == (player.x + 1, player.y) or self.pos() == (
                player.x, player.y - 1) or self.pos() == (player.x, player.y + 1):
            return True

    def action(self, player):
        if self.agressive:
            # find location of player and move to him
            pass
        else:
            if self.attacked:
                self.able_to_attack = self.check_range(player)
                if self.able_to_attack:
                    player.hp = player.hp - self.attack
