class Tile:

    def __init__(self, passable, asset, mob, item):
        self.passable = passable
        self.tile = asset
        if mob:
            self.mob = mob
        for it in item:
            self.item.append(it)

