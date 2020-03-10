from player import *

screenSize(800, 600)
playsprite = newSprite("szkielet/preview.png")

a = Player(playsprite)
colour = parseColour('black')
setBackgroundColour(colour)
a.show()
a.display(100, 200)

endWait()
