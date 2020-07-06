import pygame
from src.globals import *


class Draw_damage:
    def __init__(self, logika, app):
        self.logika = logika
        self.app = app
        self.screen = pygame.Surface((config.grid_x * config.tile_size, config.grid_y * config.tile_size))
        self.screen.fill([0, 0, 0])
        self.screen.set_colorkey([0, 0, 0])
        self.lx = 0
        self.ly = 0

    def draw_damage(self, mob):
        f = pygame.font.Font(None, 16)
        s = f.render("-%d" % (mob.hp_last-mob.hp), True, (255, 0, 0))
        self.screen.blit(s, ((mob.x - self.logika.gracz.x + 8) * 32,
                             (mob.y - self.logika.gracz.y + 8) * 32 - 16, 30, 30))
        mob.hp_last = mob.hp

    def draw_into(self):
        if self.lx != self.logika.gracz.x or self.ly != self.logika.gracz.y:
            self.lx = self.logika.gracz.x
            self.ly = self.logika.gracz.y
            self.timer_run()
        return self.screen

    def timer_run(self):
        self.screen.fill([0, 0, 0])
        self.screen.set_colorkey([0, 0, 0])
        pos_x, pos_y = self.logika.gracz.pos()
        pos_x = pos_x-7
        pos_y = pos_y-7
        mobs = []
        for i in range(pos_x, pos_x+15):
            for j in range(pos_y, pos_y+15):
                if maps.get(self.logika.gracz.mmap).get_tile(i, j).mob:
                    mobs.append(maps.get(self.logika.gracz.mmap).get_tile(i, j).mob)
        for a in mobs:
            if a.hp_last != a.hp:
                self.draw_damage(a)
