from src.logs.logs import Logs
from src.gfx.assets import Asset

class Config:
    def __init__(self):
        """
        wymiary wyswietlanego obszaru mapy, powinny byc nieparzyste
        """
        self.grid_x = 17
        self.grid_y = 17
        self.tile_size = 32

log = Logs()
asset = Asset()
config = Config()