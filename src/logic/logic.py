from src.mobs.player.player import Player
from src.globals import maps


class Logic():

    def __init__(self):
        self.gracz = Player(5,5,"mapa",100,20,1,"ludek")
        self.wrogowie = []
        self.wave = 0
        self.wave_active = False

    def check_interactions(self,tile,panel,app,mouse):
        if tile.mob:
            #print("is mob")
            #if mob is clicked
            #if mob is next to player u are able to attack
            self.gracz.interaction_attack(tile.mob,mouse,self)
        else:
            #print("else")
            #item/ground
            pass
        panel.resolve(mouse,self,app)

    def set_enemies(self):
        for x in range(self.gracz.x-7,self.gracz.x+7):
            for y in range(self.gracz.y-7,self.gracz.y+7):
                tile = maps.get(self.gracz.mmap).get_tile(x,y)
                if tile.mob and tile.mob != self.gracz:
                    already_in = False
                    for a in self.wrogowie:
                        if a == tile.mob:
                            already_in = True
                    if not already_in:
                        self.wrogowie.append(tile.mob)
                    

    def mob_move(self):
        #move every enemy towards the player
        if len(self.wrogowie) > 0:
            print(self.wrogowie[0].find_path(self.gracz.x,self.gracz.y))
        #pass
    def mob_attack(self,mob):
        mob.action(self.gracz)

    def mobs_routine(self):
        for a in self.wrogowie:
            a.action(self.gracz)

            

