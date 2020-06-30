class Player:
    sprite = pygame.sprite.Sprite

    def __init__(self, sprite, x, y, movement_speed):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.hp = 100
        self.eq = []
        self.movement_speed = movement_speed

    def show(self):
        showSprite(self.sprite)

    def move(self, x, y):
        moveSprite(self.sprite, x, y)

    def pick_item(self, item):
        self.eq.append(item)

    def drop_item(self):
        pass

    def attack(self, mob):
        pass
