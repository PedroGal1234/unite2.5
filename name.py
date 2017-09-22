#Pedro gallino
#9/22/17
#name.py - asks user their name and for a backround color

from ggame import *

name = input('Enter your name: ')
RGBcode = input('Enter RGB code with 0x infront: ')

color = Color(RGBcode,1)
black = Color(0x000000,1)
white = Color(0xffffff,1)

outline = LineStyle(1,color)

if RGBcode == '0x000000':
    text = TextAsset(name, fill = white, style='bold 50pt Arial')
    backround = RectangleAsset(1000,1000,outline,color)
else:
    text = TextAsset(name, fill = black, style='bold 50pt Arial')
    backround = RectangleAsset(1000,1000,outline,color)

Sprite(backround)
Sprite(text,(400,300))

App().run()


