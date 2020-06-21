import pygame
from pygame.locals import *
from src.map.map import Map
from src.globals import *

class Text:
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
        App.screen.blit(self.img, self.rect)
        

class App:
    """Create a single-window app with multiple scenes."""
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        flags = RESIZABLE
        App.scenes = []
        App.scene = None
        App.screen = pygame.display.set_mode((640, 320), flags)
        App.running = True

        self.map = Map("mapa")
        self.assets = asset
        self.assets.convert()

    def test_screen(self):
        """INITIALIZE STARTING SCREEN"""
        Scene()
        App.scene = App.scenes[App.scene.id]
        App.scene.nodes.append(Text("PRZYCISK",pos=(100,100)))
        App.scene.draw()

    def run(self):
        """Run the main event loop."""
        while App.running:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.test_screen()
                        #move up
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

        pygame.quit()


class Scene:
    id = 0
    bg = Color('gray')

    def __init__(self, *args, **kwargs):
        App.scenes.append(self)
        App.scene = self
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg

    def __str__(self):
        return "Scene {}".format(self.id)

    def draw(self):
        App.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()
