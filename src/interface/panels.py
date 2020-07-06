import pygame
from src.globals import *


class RightPanel:

    def __init__(self):
        self.R1 = MobPanel()
        self.Pp = PlayerPanel()
        self.clicked_tile = None
        self.wave_panel = WavePanel()
        self.inventory_panel = InventoryPanel()

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

    def show_panels(self, app, logika):
        self.Pp.show_player(app, logika)
        self.wave_panel.show_wave(app, logika)
        self.inventory_panel.show_inventory(app,logika)


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
        self.hp_full = asset.get('serduszko_pelne')
        self.hp_empty = asset.get('serduszko_0')
        self.hp_23 = asset.get('serduszko_23')
        self.hp_13 = asset.get('serduszko_13')

    def show_player(self, app, logika):
        textRec = pygame.draw.rect(app.screen, (0, 0, 0), (0, 544, 150, 640 - 543))
        f = pygame.font.Font(None, 16)
        s = f.render("Player", True, (0, 255, 255))
        #hp = f.render(("HP: %d" % logika.gracz.hp), True, (255, 255, 255))
        pygame.draw.rect(app.screen, (0, 0, 0), textRec)
        app.screen.blit(s, textRec)
        hpRec1 = textRec.move(0, 16)
  #      app.screen.blit(self.hp_full,hpRec1)
        hpRec2 = hpRec1.move(16,0)
 #       app.screen.blit(self.hp_full,hpRec2)
        hpRec3 = hpRec2.move(16,0)
#        app.screen.blit(self.hp_full,hpRec3)
        #app.screen.blit(hp, hpRec)
        self.resolve_hp(app,logika,hpRec1,hpRec2,hpRec3)
        at = f.render(("Attack: %d" % logika.gracz.attack), True, (255, 255, 255))
        atRec = hpRec1.move(0, 16)
        app.screen.blit(at, atRec)
        ms = f.render(("Movement speed: %d" % logika.gracz.movement), True, (255, 255, 255))
        msRec = atRec.move(0, 11)
        app.screen.blit(ms, msRec)


    def resolve_hp(self,app,logika,r1,r2,r3):
        if logika.gracz.hp > 80:
            #blit 3 hp full
            app.screen.blit(self.hp_full,r1)
            app.screen.blit(self.hp_full,r2)
            app.screen.blit(self.hp_full,r3)
        elif logika.gracz.hp > 60:
            #blit 2 hp full and another depending on state
            app.screen.blit(self.hp_full,r1)
            app.screen.blit(self.hp_full,r2)
            if logika.gracz.hp - 60 > 9:
                #blit 2/3hp
                app.screen.blit(self.hp_23,r3)
            elif logika.gracz.hp - 60 > 0:
                #blit 1/3hp
                app.screen.blit(self.hp_13,r3)
            else:
                #blit empty heart
                app.screen.blit(self.hp_empty,r3)
        elif logika.gracz.hp > 30:
            #blit 1 hp full and another depending on state
            app.screen.blit(self.hp_full,r1)
            if logika.gracz.hp - 30 > 9:
                #blit 2/3hp and empty heart
                app.screen.blit(self.hp_23,r2)
            elif logika.gracz.hp - 30 > 0:
                #blit 1/3 hp and empty heart
                app.screen.blit(self.hp_13,r2)
            app.screen.blit(self.hp_empty,r3)
        else:
            #blit 1 heart depending on state and 2 empty
            if logika.gracz.hp == 0:
                app.screen.blit(self.hp_empty,r1)
            else:
                if logika.gracz.hp > 20:
                    app.screen.blit(self.hp_23,r1)
                else:
                    app.screen.blit(self.hp_13,r1)
            app.screen.blit(self.hp_empty,r2)
            app.screen.blit(self.hp_empty,r3)


            
    

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

class InventoryPanel:
    def __init__(self):
        self.rec = pygame.Rect(150,544,394,640-543)
        self.empty_inv = asset.get('empty_inv')


    def show_inventory(self,app,logika):
        textRec = pygame.draw.rect(app.screen,(0,0,0),self.rec)
        f = pygame.font.Font(None,16)
        s = f.render("Inventory ",True, (0,255,255))
        #blit inventory
        first_field = textRec.move(0,16)
        pygame.draw.rect(app.screen,(0,0,0), textRec)
        app.screen.blit(s,textRec)
        for j in range(4):
            for i in range(3):
                app.screen.blit(self.empty_inv,first_field)
                first_field = first_field.move(16,0)
            first_field = first_field.move(-48,16)
