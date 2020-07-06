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

    def lethal(self,logika):
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

    '''def calculate_path(self, x, y):
        class DijkstraStruct:
            def __init__(self, pos, dist):
                self.pos = pos
                self.dist = dist

        curr = (self.x, self.y)
        dest = (x, y)
        visited = set()
        dist = 0
        to_check = [curr]
        while True:
            curr = to_check[0]
            to_check.pop(0)'''


    def find_path(self, dest_x, dest_y):
        """
        :param: współrzędne gracza, do którego szukamy najkrótszej ścieżki
        :return: lista z najkrótszą ścieżką!
        """
        neighbours = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()
        queue.append((self.pos()))
        path = {}
        result_path = deque()
        path[self.pos()] = None

        while len(queue) > 0:
            current_x, current_y = queue.popleft()
            if current_x == dest_x and current_y == dest_y:
                break
            for neighbour_x, neighbour_y in neighbours:
                is_mob = maps.get(self.mmap).get_tile(current_x+neighbour_x, current_y+neighbour_y).mob
                is_passable = maps.get(self.mmap).get_tile(current_x+neighbour_x, current_y+neighbour_y).passable
                if is_passable and not is_mob and (current_x+neighbour_x, current_y+neighbour_y) not in path:
                    queue.append((current_x+neighbour_x, current_y+neighbour_y))
                    path[(current_x+neighbour_x, current_y+neighbour_y)] = (current_x, current_y)

        result_path.appendleft((dest_x, dest_y))
        current_vertex = path[(dest_x, dest_y)]
        while current_vertex != self.pos():
            current_vertex = path[current_vertex]
            result_path.appendleft(current_vertex)

        return result_path



class Enemy(Mob):
    def __init__(self, x, y, mmap, hp, attack, movement, asset=None, name=None):
        super().__init__(x, y, mmap, hp, attack, movement, asset, name)
        self.agressive = False
        self.attacked = False
        self.able_to_attack = False
    
    def check_range(self, player):
        if self.pos() == (player.x-1,player.y) or self.pos() == (player.x+1,player.y) or self.pos() == (player.x,player.y-1) or self.pos() == (player.x,player.y+1):
            return True

    def action(self,player):
        if self.agressive:
            #find location of player and move to him
            pass
        else:
            if self.attacked:
                self.able_to_attack = self.check_range(player) 
                if self.able_to_attack:
                    player.hp = player.hp - self.attack

