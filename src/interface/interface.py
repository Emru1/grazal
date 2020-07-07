import pygame
from pygame.locals import *

from src.globals import *
from src.interface.damage_drawing import Draw_damage
from src.interface.event_handler import event_handler
from src.interface.map_drawing import MapSurface
from src.interface.mob_drawing import MobSurface
from src.interface.panels import RightPanel
from src.logic.logic import Logic
from src.map.map import Map


class App:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        pygame.mixer.quit()
        flags = RESIZABLE
        self.scenes = []
        self.scene = None
        self.screen = pygame.display.set_mode((640, 640), flags)
        self.running = True
        maps.add("mapa", Map("mapa"))
        self.assets = asset
        self.assets.convert()
        self.map_screen = MapSurface(maps.get("mapa"))
        self.mob_screen = MobSurface(maps.get("mapa"))
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.mob_pane = False
        self.logika = Logic()
        self.panel = RightPanel()
        self.draw_damage = Draw_damage(self.logika, self)
        timer.add(1000, self.draw_damage)

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mous = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        f = pygame.font.Font(None, 32)
        s = f.render(msg, True, [0, 0, 0])
        text_rec = s.get_rect()
        text_rec.center = (x // 2, y // 2)
        if text_rec.collidepoint(mous[0], mous[1]):
            pygame.draw.rect(self.screen, ac, text_rec)
            if click[0]:
                action()
        else:
            pygame.draw.rect(self.screen, ic, text_rec)
        self.screen.blit(s, text_rec)

    def intro(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill((255, 255, 255))
            self.button("Play", 640, 300, 100, 100, (255, 0, 0), (0, 255, 0), self.game_loop)
            self.button("Options", 640, 500, 100, 100, (255, 0, 0), (0, 255, 0))
            self.button("Exit", 640, 700, 100, 100, (255, 0, 0), (0, 255, 0), quit)
            pygame.display.update()

    def game_loop(self):
        while self.running:
            self.screen.blit(self.map_screen.draw(self.logika.gracz.x, self.logika.gracz.y), (0, 0))
            self.screen = self.mob_screen.draw(self.screen, self.logika.gracz.x, self.logika.gracz.y)
            self.screen.blit(self.draw_damage.draw_into(), (0, 0))
            self.panel.show_panels(self, self.logika)
            # self.mob_panel(maps.get(logika.gracz.mmap).get_tile(int(pygame.mouse.get_pos()[0]/32)-1,int(pygame.mouse.get_pos()[1]/32)-1))
            event_handler(self, self.logika, maps.get("mapa"), self.panel)
            # EVENT LOOP FUNCTION HERE
            self.clock.tick(60)
            timer.run()
            pygame.display.flip()

    def run(self):
        """Run the main event loop."""
        self.intro()
        pygame.quit()
