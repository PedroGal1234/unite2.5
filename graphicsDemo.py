#Pedro Gallino
#9/20.17
#graphicsDemo.py - intro to graphics using ggam

from ggame import *

red = Color(0xff0000,1) #(color, transperancy)
green = Color(0x00ff00,1)
blue = Color(0x000ff,1)
black = Color(0x000ff,1)

blackOutline = LineStyle(1,black) #(pixels, color)

redRectangle = RectangleAsset(200,100,blackOutline,red) #(width, height, outline, fill)

Sprite(redRectangle)

App().run()
