#Pedro Gallino
#9/22/17
#yield.py - displays a yield line

from ggame import *

red = Color(0xff0000,1)
white = Color(0xffffff,1)

redOutline = LineStyle(1,red)
whiteOutline = LineStyle(1,white)

redTriangle = PolygonAsset([(0,0),(220,400),(440,0)],redOutline,red)
whiteTriangle = PolygonAsset([(-30,-40),(110,200),(250,-40)],whiteOutline,white)
text = TextAsset('YIELD', fill=red, style='bold 40pt Times')

Sprite(redTriangle,(325,100))
Sprite(whiteTriangle,(435,200))
Sprite(text,(464,180))

App().run()