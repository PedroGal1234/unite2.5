#Pedro Gallino
#9/26/17
#olympics.py - shows the olympic rings

from ggame import *

blue = Color(0x000ff,1)
yellow = Color(0xffff00,1)
black = Color(0x00000,1)
green = Color(0x00ff00,1)
red = Color(0xff0000,1)
white = Color(0xffffff,0)

blueOutline = LineStyle(10,blue)
yellowOutline = LineStyle(10,yellow)
blackOutline = LineStyle(10,black)
greenOutline = LineStyle(10,green)
redOutline = LineStyle(10,red)

blueCircle = CircleAsset(80,blueOutline,white)
yellowCircle = CircleAsset(80,yellowOutline,white)
blackCircle = CircleAsset(80,blackOutline,white)
greenCircle = CircleAsset(80,greenOutline,white)
redCircle = CircleAsset(80,redOutline,white)

Sprite(blueCircle,(200,150))
Sprite(yellowCircle,(300,210))
Sprite(blackCircle,(400,150))
Sprite(greenCircle,(500,210))
Sprite(redCircle,(600,150))

App().run()
