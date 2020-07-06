import pygame
from src.globals import *


class RightPanel:

    def __init__(self):
        self.R1 = MobPanel()
        self.Pp = PlayerPanel()
        self.clicked_tile = None
        self.wave_panel = WavePanel()

    def resolve(self, mouse, logika, app):
        self.wave_panel.show_wave(app, logika)
        self.clicked_tile = maps.get(logika.gracz.mmap).get_tile(int(mouse[0] / 32) - 8 + logika.gracz.x,
                                                                 int(mouse[1] / 32) - 8 + logika.gracz.y)
        if self.clicked_tile.mob:
            # check if your not clicking on the player
            if self.clicked_tile.mob.x == logika.gracz.x and self.clicked_tile.mob.y == logika.gracz.y:
                self.R1.show_player(app, logika)
            else:
                self.R1.tile_is_mob = True
                self.R1.show(app, self.clicked_tile)
                # make mob_panel appear
        else:
            self.R1.tile_is_mob = False
            self.R1.show_default(app)


class MobPanel:

    def __init__(self):
        self.rec = pygame.Rect(544, 0, 640 - 543, 100)
        self.tile_is_mob = False

    def show(self, app, tile):
        if self.tile_is_mob:
            textRec = pygame.draw.rect(app.screen, (100, 255, 0), (544, 0, 640 - 543, 100))
            f = pygame.font.Font(None, 16)
            s = f.render(tile.mob.name, True, (0, 255, 255))
            hp = f.render(("HP: %d" % tile.mob.hp), True, (255, 255, 255))
            pygame.draw.rect(app.screen, (0, 0, 0), textRec)
            app.screen.blit(s, textRec)
            hpRec = textRec.move(0, 11)
            app.screen.blit(hp, hpRec)
            at = f.render(("Attack: %d" % tile.mob.attack), True, (255, 255, 255))
            atRec = hpRec.move(0, 11)
            app.screen.blit(at, atRec)
        else:
            self.show_default(app)

    def show_default(self, app):
        textRec = pygame.draw.rect(app.screen, (0, 0, 0), (544, 0, 640 - 543, 100))
        f = pygame.font.Font(None, 16)
        s = f.render("Just a ground", True, (255, 255, 255))
        app.screen.blit(s, textRec)

    def show_player(self, app, logika):
        textRec = pygame.draw.rect(app.screen, (100, 255, 0), (544, 0, 640 - 543, 100))
        f = pygame.font.Font(None, 16)
        s = f.render("Player", True, (0, 255, 255))
        hp = f.render(("HP: %d" % logika.gracz.hp), True, (255, 255, 255))
        pygame.draw.rect(app.screen, (0, 0, 0), textRec)
        app.screen.blit(s, textRec)
        hpRec = textRec.move(0, 11)
        app.screen.blit(hp, hpRec)
        at = f.render(("Attack: %d" % logika.gracz.attack), True, (255, 255, 255))
        atRec = hpRec.move(0, 11)
        app.screen.blit(at, atRec)


class PlayerPanel:
    def __init__(self):
        self.rec = pygame.Rect(0, 544, 400, 640 - 543)

    def show_player(self, app, logika):
        textRec = pygame.draw.rect(app.screen, (0, 0, 0), (0, 544, 150, 640 - 543))
        f = pygame.font.Font(None, 16)
        s = f.render("Player", True, (0, 255, 255))
        hp = f.render(("HP: %d" % logika.gracz.hp), True, (255, 255, 255))
        pygame.draw.rect(app.screen, (0, 0, 0), textRec)
        app.screen.blit(s, textRec)
        hpRec = textRec.move(0, 11)
        app.screen.blit(hp, hpRec)
        at = f.render(("Attack: %d" % logika.gracz.attack), True, (255, 255, 255))
        atRec = hpRec.move(0, 11)
        app.screen.blit(at, atRec)
        ms = f.render(("Movement speed: %d" % logika.gracz.movement), True, (255, 255, 255))
        msRec = atRec.move(0, 11)
        app.screen.blit(ms, msRec)


class WavePanel:
    def __init__(self):
        self.rec = pygame.Rect(544, 544, 400, 640 - 543)

    def show_wave(self, app, logika):
        textRec = pygame.draw.rect(app.screen, (0, 0, 0), self.rec)
        f = pygame.font.Font(None, 16)
        s = f.render(("Wave: %d" % logika.wave), True, (255, 255, 255))
        pygame.draw.rect(app.screen, (0, 0, 0), textRec)
        app.screen.blit(s, textRec)
        enemies_left = f.render(("Enemies to kill: %d" % len(logika.wrogowie)), True, (255, 255, 255))
        enemiesRec = textRec.move(0, 11)
        app.screen.blit(enemies_left, enemiesRec)
