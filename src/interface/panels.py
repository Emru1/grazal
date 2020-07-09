import pygame

from src.globals import *


class RightPanel:

    def __init__(self):
        self.R1 = MobPanel()
        self.Pp = PlayerPanel()
        self.clicked_tile = None
        self.wave_panel = WavePanel()
        self.inventory_panel = InventoryPanel()
        self.instructions = InstructionPanel()

    def resolve(self, mouse, logika, app):
        self.clicked_tile = maps.get(logika.gracz.mmap).get_tile(int(mouse[0] / 32) - 8 + logika.gracz.x,
                                                                 int(mouse[1] / 32) - 8 + logika.gracz.y)
        # self.wave_panel.resolve_hover(app, logika,self.inventory_panel, mouse)
        if (0 < mouse[0] < config.grid_x * config.tile_size) and (0 < mouse[1] < config.grid_y * config.tile_size):
            if self.clicked_tile.mob:
                self.R1.show(app, self.clicked_tile)
            else:
                self.R1.show_default(app, self.clicked_tile)
        else:
            # kliknieto na element poza mapa
            if self.inventory_panel.rec.collidepoint(mouse):
                self.inventory_panel.resolve(app, logika, mouse)

    def show_panels(self, app, logika):
        self.Pp.show_player(app, logika)
        self.wave_panel.show_wave(app)
        self.inventory_panel.show_equiped_inventory(app, logika)
        self.inventory_panel.show_inventory(app, logika)
        self.instructions.show_instruction(app)
        if not self.clicked_tile:
            self.R1.show_default(app, self.clicked_tile)


class BasePanel:

    def __init__(self):
        self.left_up = asset.get('left_up')
        self.center_up = asset.get('center_up')
        self.right_up = asset.get('right_up')
        self.right_center = asset.get('right_center')
        self.right_down = asset.get('right_down')
        self.center_down = asset.get('center_down')
        self.left_down = asset.get('left_down')
        self.left_center = asset.get('left_center')
        self.center = asset.get('center')

    def blit_background(self, app, width, height, rec):
        # REC to pygame.rec reprezentuje lewy gorny rog dla rysowanego panelu (x,y,16,16)
        # blit left corner
        app.screen.blit(self.left_up, rec)
        for i in range(width - 2):
            rec = rec.move(16, 0)
            app.screen.blit(self.center_up, rec)
        rec = rec.move(16, 0)
        app.screen.blit(self.right_up, rec)
        for j in range(height - 2):
            rec = rec.move((width - 1) * -16, 16)
            app.screen.blit(self.left_center, rec)
            for i in range(width - 2):
                rec = rec.move(16, 0)
                app.screen.blit(self.center, rec)
            rec = rec.move(16, 0)
            app.screen.blit(self.right_center, rec)
        rec = rec.move((width - 1) * -16, 16)
        app.screen.blit(self.left_down, rec)
        for i in range(width - 2):
            rec = rec.move(16, 0)
            app.screen.blit(self.center_down, rec)
        rec = rec.move(16, 0)
        app.screen.blit(self.right_down, rec)


class MobPanel(BasePanel):
    def __init__(self):
        super().__init__()
        self.rec = pygame.Rect(544, 0, 640 - 543, 100)

    def show(self, app, tile):
        self.blit_background(app, 6, 6, pygame.Rect(544, 0, 16, 16))
        nameRec = pygame.Rect(570, 16, 1, 1)
        f = pygame.font.Font(None, 16)
        s = f.render(tile.mob.name, True, (0, 0, 0), None)
        app.screen.blit(s, nameRec)
        hpRec = nameRec.move(-20, 16)
        s = f.render("HP: %d" % tile.mob.hp, True, (0, 0, 0), None)
        app.screen.blit(s, hpRec)
        attRec = hpRec.move(0, 16)
        s = f.render("Attack: %d" % tile.mob.attack, True, (0, 0, 0), None)
        app.screen.blit(s, attRec)

    def show_default(self, app, tile):
        self.blit_background(app, 6, 6, pygame.Rect(544, 0, 16, 16))

    def show_player(self, app, logika):
        self.blit_background(app)


class PlayerPanel(BasePanel):
    def __init__(self):
        super().__init__()
        self.rec = pygame.Rect(0, 544, 400, 640 - 543)
        self.hp_full = asset.get('serduszko_pelne')
        self.hp_empty = asset.get('serduszko_0')
        self.hp_23 = asset.get('serduszko_23')
        self.hp_13 = asset.get('serduszko_13')

    def show_player(self, app, logika):
        self.blit_background(app, 10, 6, pygame.Rect(0, 544, 16, 16))
        nameRec = pygame.Rect(50, 550, 0, 0)
        f = pygame.font.Font(None, 16)
        s = f.render("Gracz", True, (0, 0, 0), None)
        app.screen.blit(s, nameRec)
        hpRec1 = pygame.Rect(8, 566, 16, 16)
        hpRec2 = hpRec1.move(16, 0)
        hpRec3 = hpRec2.move(16, 0)
        self.resolve_hp(app, logika, hpRec1, hpRec2, hpRec3)
        hpRec = hpRec3.move(16, 2)
        app.screen.blit(f.render("HP: %d / %d" % (logika.gracz.hp, logika.gracz.hp_max), True, (0, 0, 0), None), hpRec)
        app.screen.blit(f.render("Attack: %d" % logika.gracz.attack, True, (0, 0, 0), None), hpRec1.move(0, 16))
        app.screen.blit(f.render("Armor: %d" % logika.gracz.armor_val, True, (0, 0, 0), None), hpRec1.move(0, 32))

    def resolve_hp(self, app, logika, r1, r2, r3):
        if logika.gracz.hp > 80:
            # blit 3 hp full
            app.screen.blit(self.hp_full, r1)
            app.screen.blit(self.hp_full, r2)
            app.screen.blit(self.hp_full, r3)
        elif logika.gracz.hp > 60:
            # blit 2 hp full and another depending on state
            app.screen.blit(self.hp_full, r1)
            app.screen.blit(self.hp_full, r2)
            if logika.gracz.hp - 60 > 9:
                # blit 2/3hp
                app.screen.blit(self.hp_23, r3)
            elif logika.gracz.hp - 60 > 0:
                # blit 1/3hp
                app.screen.blit(self.hp_13, r3)
            else:
                # blit empty heart
                app.screen.blit(self.hp_empty, r3)
        elif logika.gracz.hp > 30:
            # blit 1 hp full and another depending on state
            app.screen.blit(self.hp_full, r1)
            if logika.gracz.hp - 30 > 9:
                # blit 2/3hp and empty heart
                app.screen.blit(self.hp_23, r2)
            elif logika.gracz.hp - 30 > 0:
                # blit 1/3 hp and empty heart
                app.screen.blit(self.hp_13, r2)
            app.screen.blit(self.hp_empty, r3)
        else:
            # blit 1 heart depending on state and 2 empty
            if logika.gracz.hp == 0:
                app.screen.blit(self.hp_empty, r1)
            else:
                if logika.gracz.hp > 20:
                    app.screen.blit(self.hp_23, r1)
                else:
                    app.screen.blit(self.hp_13, r1)
            app.screen.blit(self.hp_empty, r2)
            app.screen.blit(self.hp_empty, r3)


class WavePanel(BasePanel):
    def __init__(self):
        super().__init__()
        self.rec = pygame.Rect(544, 544, 400, 640 - 543)
        self.name = None
        self.description = None

        #  def show_wave(self, app, logika):
        pass
        # self.blit_background(app, 6, 6, pygame.Rect(544, 544, 16, 16))

    def resolve_hover(self, app, logika, inwentory, mouse):
        if inwentory.armor_rec.collidepoint(mouse):
            # najechano myszka na armor
            if logika.gracz.armor:
                self.name = inwentory.armor.name
                self.description = inwentory.armor.description
            else:
                self.name = None
                self.description = None
        elif inwentory.weapon_rec.collidepoint(mouse):
            # najechano myszka na bron
            if logika.gracz.weapon:
                self.name = inwentory.weapon.name
                self.description = inwentory.weapon.description
            else:
                self.name = None
                self.description = None
        elif logika.gracz.eq_count != 0:
            for i in range(logika.gracz.eq_count):
                if inwentory.inventory_rec[i].collidepoint(mouse):
                    # Wyswietl informacje o bierzacej pozycji myszki
                    self.name = logika.gracz.eq[i].name
                    self.description = logika.gracz.eq[i].description
        else:
            self.name = None
            self.description = None

    def show_wave(self, app):
        def blit_text(surface, text, pos, font, color=pygame.Color('black')):
            words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
            space = font.size(' ')[0]  # The width of a space.
            max_width, max_height = surface.get_size()
            x, y = pos
            for line in words:
                for word in line:
                    word_surface = font.render(word, True, color, None)
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= max_width:
                        x = pos[0]  # Reset the x.
                        y += word_height  # Start on new row.
                    surface.blit(word_surface, (x, y))
                    x += word_width + space
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.

        self.blit_background(app, 6, 6, pygame.Rect(544, 544, 16, 16))
        textRec = pygame.Rect(544 + 5, 544 + 10, 32, 32)
        if self.name and self.description:
            blit_text(app.screen, self.name + '\n\n' + self.description, (549, 554), pygame.font.Font(None, 16),
                      (0, 0, 0))
        elif self.name and not self.description:
            blit_text(app.screen, self.name, (549, 554), pygame.font.Font(None, 16), (0, 0, 0))


class InventoryPanel(BasePanel):
    def __init__(self):
        super().__init__()
        self.rec = pygame.Rect(544, 640 - 544, 640 - 543, 200)
        self.weapon_rec = pygame.Rect(598, 640 - 543 + 36, 32, 32)
        self.armor_rec = pygame.Rect(550, 640 - 543 + 36, 32, 32)
        self.empty_inv = asset.get('empty_inv')
        self.inventory_rec = []

    def show_equiped_inventory(self, app, logika):
        self.blit_background(app, 6, 6, pygame.Rect(544, 640 - 544, 16, 16))
        textRec = pygame.Rect(567, 640 - 544 + 15, 20, 20)
        f = pygame.font.Font(None, 19)
        s = f.render("Equiped", True, (0, 0, 0), None)
        app.screen.blit(s, textRec)
        ArmorText = pygame.Rect(550, 640 - 543 + 68, 20, 20)
        k = pygame.font.Font(None, 16)
        s = k.render("Armor", True, (0, 0, 0), None)
        app.screen.blit(s, ArmorText)
        if logika.gracz.armor:
            pass
            # blit item
        else:
            app.screen.blit(self.empty_inv, self.armor_rec)
        WeaponText = pygame.Rect(590, 640 - 543 + 68, 20, 20)
        s = k.render("Weapon", True, (0, 0, 0), None)
        app.screen.blit(s, WeaponText)
        if logika.gracz.weapon:
            pass
        else:
            app.screen.blit(self.empty_inv, self.weapon_rec)

    def show_inventory(self, app, logika):
        self.blit_background(app, 6, 22, pygame.Rect(544, 640 - 544 + 16 * 6, 16, 16))
        f = pygame.font.Font(None, 19)
        s = f.render("Inventory", True, (0, 0, 0), None)
        textRec = pygame.Rect(563, 640 - 544 + 16 * 6 + 13, 16, 16)
        app.screen.blit(s, textRec)
        first = pygame.Rect(555, 640 - 544 + 16 * 6 + 36, 32, 32)
        # blit empty_inventory then blit items
        first = first.move(-32, 0)
        for i in range(9):
            for i in range(2):
                first = first.move(34, 0)
                self.inventory_rec.append(first)
                app.screen.blit(self.empty_inv, first)
            first = first.move(2 * (-34), 34)
        for i in range(len(logika.gracz.eq)):
            app.screen.blit(asset.get(logika.gracz.eq[i].asset), self.inventory_rec[i])

    def resolve(self, app, logika, mouse):
        # sprawdz czy klikano lub najechano na jeden z elementow inwentarza
        # j esli gracz nie ma zadnego ekwipunku nie sprawdzaj
        if logika.gracz.eq_count != 0:
            # gracz ma itemy sprawdz czy najechano na kwadrat z itemem
            for i in range(logika.gracz.eq_count):
                if self.inventory_rec[i].collidepoint(mouse):
                    if logika.gracz.eq[i].edible:
                        # itemek jadalny
                        logika.gracz.eq[i].use(logika.gracz)
                        logika.gracz.eq.remove(logika.gracz.eq[i])
                        logika.gracz.eq_count = logika.gracz.eq_count - 1
                    else:
                        if not logika.gracz.eq[i].equip(logika.gracz):
                            logika.gracz.eq_count = logika.gracz.eq_count - 1
                        else:
                            temp = logika.gracz.eq[i]
                            if logika.gracz.eq[i].armor:
                                logika.gracz.eq[i] = logika.gracz.armor
                                logika.gracz.armor = temp
                            elif logika.gracz.eq[i].weapon:
                                logika.gracz.eq[i] = logika.gracz.weapon
                                logika.gracz.weapon = temp
                        logika.gracz.eq.remove(logika.gracz.eq[i])
        if self.weapon_rec.collidepoint(mouse):
            # gracz klika na aktualna bron
            if logika.gracz.weapon != None:
                logika.gracz.eq_count = logika.gracz.eq_count + 1
                logika.gracz.eq.append(logika.gracz.weapon)
                logika.gracz.weapon.unequip(logika.gracz)
        if self.armor_rec.collidepoint(mouse):
            # gracz klika na aktualna zbroje
            if logika.gracz.armor != None:
                logika.gracz.eq_count = logika.gracz.eq_count + 1
                logika.gracz.eq.append(logika.gracz.armor)
                logika.gracz.armor.unequip(logika.gracz)


class InstructionPanel(BasePanel):
    def __init__(self):
        super().__init__()
        self.rec = pygame.Rect(160, 544, 80, 200)

    def show_instruction(self, app):
        self.blit_background(app, 24, 6, pygame.Rect(160, 544, 16, 16))
        f = pygame.font.Font(None, 16)
        s = f.render("Instructions:", True, (0, 0, 0))
        first_line = pygame.Rect(164, 550, 80, 10)
        app.screen.blit(s, first_line)
        s = f.render("You can move by using WASD", True, (0, 0, 0), None)
        first_line = first_line.move(0, 16)
        app.screen.blit(s, first_line)
        s = f.render("Interact by using left mouse button", True, (0, 0, 0), None)
        first_line = first_line.move(0, 16)
        app.screen.blit(s, first_line)
        s = f.render("Left click on the items in inventory to equip/unequip", True, (0, 0, 0), None)
        first_line = first_line.move(0, 16)
        app.screen.blit(s, first_line)
        s = f.render("Right click on the item to delete from inventory", True, (0, 0, 0), None)
        first_line = first_line.move(0, 16)
        app.screen.blit(s, first_line)
