from src.globals import maps



class Mob:
    """
    uniwersalna klasa symbolizująca generycznego moba
    może to być postać gracza, przeciwnik lub NPC
    """
    def __init__(self, x, y, mmap, hp, attack, movement, asset=None):
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

        maps.get(self.mmap).get_tile(self.x, self.y).mob = self

    

    def lethal(self):
        self.hp = 0
        maps.get(self.mmap).get_tile(self.x, self.y).mob = None
        
            
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


class Enemy(Mob):
    def __init__(self, x, y, mmap, hp, attack, movement, asset=None):
        super().__init__(x, y, mmap, hp, attack, movement, asset)
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
                self.able_to_attack = check_range(self,player) 
                if self.able_to_attack:
                    player.hp = player.hp - self.attack