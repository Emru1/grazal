from src.mobs.player.player import Player

class Logic():

    def __init__(self):
        self.gracz = Player(500,500,"mapa",100,20,1,"ludek")
        self.wrogowie = []
        self.wave = 0
        self.wave_active = False

    
