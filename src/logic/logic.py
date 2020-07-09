from src.globals import maps, timer
from src.mobs.player.player import Player


class Logic:
    def __init__(self):
        self.gracz = Player(5, 5, "mapa", 90, 20, 1, "zz")
        self.wrogowie = []
        self.wave = 0
        self.wave_active = False
        timer.add(800, self)

    def check_conditions(self):
        if self.gracz.hp > 0:
            return True
        else:
            return False

    def check_interactions(self, tile, panel, app, mouse):
        if tile.mob:
            # print("is mob")
            # if mob is clicked
            # if mob is next to player u are able to attack
            self.gracz.interaction_attack(tile.mob, self)
        elif tile.obj:
            self.gracz.interaction_pickup(tile.obj, self)
        panel.resolve(mouse, self, app)

    def set_enemies(self):
        for x in range(self.gracz.x - 7, self.gracz.x + 7):
            for y in range(self.gracz.y - 7, self.gracz.y + 7):
                tile = maps.get(self.gracz.mmap).get_tile(x, y)
                if tile.mob and tile.mob != self.gracz:
                    already_in = False
                    for a in self.wrogowie:
                        if a == tile.mob:
                            already_in = True
                    if not already_in:
                        self.wrogowie.append(tile.mob)

    def mob_move(self):
        # move every enemy towards the player
        for wrog in self.wrogowie:
            shortest_path = wrog.find_path(self.gracz.x, self.gracz.y)
            if shortest_path:
                wrog.move_to(shortest_path[0], shortest_path[1])
            if wrog.check_range(self.gracz):
                wrog.action(self.gracz)
            # for step_x, step_y in shortest_path:
            #     wrog.move_to(step_x, step_y)
        # pass

    def timer_run(self):
        self.mob_move()

    def mob_attack(self, mob):
        mob.action(self.gracz)

    def mobs_routine(self):
        for a in self.wrogowie:
            a.action(self.gracz)
