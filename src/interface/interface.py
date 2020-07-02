import pygame
from pygame.locals import *
from src.map.map import Map
from src.globals import *
from src.interface.map_drawing import MapSurface
from src.interface.mob_drawing import MobSurface
from src.logic.logic import Logic
from src.interface.event_handler import event_handler

'''class Text:
    """Create a text object."""

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        """Set the Font object from name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        App.screen.blit(self.img, self.rect)'''
        

class App:
    """Create a single-window app with multiple scenes."""
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
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

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mous = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        f = pygame.font.Font(None, 32)
        s = f.render(msg, True, [0, 0, 0])
        textRec = s.get_rect()
        textRec.center = (x//2,y//2)
        if textRec.collidepoint(mous[0],mous[1]):
            pygame.draw.rect(self.screen,ac,textRec)
            if click[0] == True:
                action()
        else:
            pygame.draw.rect(self.screen,ic,textRec)
        self.screen.blit(s,textRec)

    def intro(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill((255,255,255))
            self.button("Play", 640, 300, 100, 100, (255, 0, 0), (0, 255, 0), self.game_loop)
            self.button("Options", 640, 500, 100, 100, (255, 0, 0), (0, 255, 0))
            self.button("Exit", 640, 700, 100, 100, (255, 0, 0), (0, 255, 0), quit)
            pygame.display.update()

    def right_panel(self):
        pygame.draw.rect(self.screen,(100,255,0),(544,0,640-543,100)) #minimap
        pygame.draw.rect(self.screen,(100,0,255),(544,100,640-543,200))
        pygame.draw.rect(self.screen,(100,255,0),(544,300,640-543,245))

    def game_loop(self):
        logika = Logic()
        while self.running:
            self.screen.blit(self.map_screen.draw(7, 7), (0, 0))
            self.screen = self.mob_screen.draw(self.screen, 7, 7)
            self.right_panel()
            event_handler(logika,maps.get("mapa"))
            #EVENT LOOP FUNCTION HERE
            pygame.display.flip() 

    def test_screen(self):
        """INITIALIZE STARTING SCREEN"""
        self.screen.blit(self.map_screen.draw(7, 7), (0, 0))

    def run(self):
        """Run the main event loop."""
        while self.running:  
            self.intro()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        #move up
                        pass
                    elif event.key == pygame.K_s:
                        #move down
                        pass
                    elif event.key == pygame.K_a:
                        #move left
                        pass
                    elif event.key == pygame.K_d:
                        #move right
                        pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        #Left mouse button
                        pass
                    elif event.button == 3:
                        #right mouse button
                        pass
            pygame.display.flip()

        pygame.quit()