from src.logs.logs import Logs
from src.gfx.assets import Asset


class Config:
    def __init__(self):
        """
        konfiguracja na poziomie silnika gry
        """
        # rozmiar wyswietlanego obszaru w kratkach
        self.grid_x = 17
        self.grid_y = 17
        # rozmiar grafik
        self.tile_size = 32


log = Logs()
asset = Asset()
config = Config()