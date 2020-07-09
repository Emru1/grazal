from src.gfx.assets import Asset
from src.logic.timer import Timer
from src.logs.logs import Logs
from src.map.maps_repo import Maps
from src.mobs.mobs_repo import Mobs


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
        self.mob_path = 'cfg/mobs'


log = Logs()
asset = Asset()
config = Config()
maps = Maps()
timer = Timer()
mobs = Mobs(config.mob_path)
