import pygame
from pygame.locals import *
from src.map.map import Map
from src.globals import *
from src.interface.map_drawing import MapSurface
from src.interface.mob_drawing import MobSurface
from src.logic.logic import Logic
from src.interface.event_handler import event_handler
from src.interface.panels import RightPanel



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

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mous = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        f = pygame.font.Font(None, 32)
        s = f.render(msg, True, [0, 0, 0])
        textRec = s.get_rect()
        textRec.center = (x // 2, y // 2)
        if textRec.collidepoint(mous[0], mous[1]):
            pygame.draw.rect(self.screen, ac, textRec)
            if click[0] == True:
                action()
        else:
            pygame.draw.rect(self.screen, ic, textRec)
        self.screen.blit(s, textRec)

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
        logika = Logic()
        panel = RightPanel()
        while self.running:
            self.screen.blit(self.map_screen.draw(logika.gracz.x, logika.gracz.y), (0, 0))
            self.screen = self.mob_screen.draw(self.screen, logika.gracz.x, logika.gracz.y)
            panel.Pp.show_player(self, logika)
            panel.wave_panel.show_wave(self, logika)
            panel.inventory_panel.show_inventory(self,logika)
            # self.mob_panel(maps.get(logika.gracz.mmap).get_tile(int(pygame.mouse.get_pos()[0]/32)-1,int(pygame.mouse.get_pos()[1]/32)-1))
            event_handler(self, logika, maps.get("mapa"), panel)
            logika.mob_move()
            # EVENT LOOP FUNCTION HERE
            self.clock.tick(60)
            timer.run()
            pygame.display.flip()

    def run(self):
        """Run the main event loop."""
        self.intro()
        pygame.quit()
