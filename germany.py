#Pedro gallino
#9/22/17
#germany.py - shows German flag

from ggame import *

black = Color(0x00000,1)
red = Color(0xff0000,1)
yellow = Color(0xffff00,1)


blackOutline = LineStyle(2,black)
redOutline = LineStyle(2,red)
yellowOutline = LineStyle(2,yellow)

blackRectangle = RectangleAsset(400,100,blackOutline,black)
redRectangle = RectangleAsset(400,100,redOutline,red)
yellowRectangle = RectangleAsset(400,100,yellowOutline,yellow)

Sprite(blackRectangle,(100,0))
Sprite(redRectangle,(100,100))
Sprite(yellowRectangle,(100,200))

App().run()