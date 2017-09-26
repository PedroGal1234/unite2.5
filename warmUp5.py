#Pedro Gallino
#9/20/17
#warmUp5.py - shows a dimond with name

from ggame import *


yellow = Color(0xffff00,1)
blue = Color(0x0000ff,1)

yellowOutline = LineStyle(1,yellow)

yellowDimond = PolygonAsset([(0,0),(150,150),(300,0),(150,-150)],yellowOutline,yellow)
text = TextAsset('Pedro Gallino', fill=blue, style='bold 30pt Times')

Sprite(yellowDimond,(400,350))
Sprite(text,(490,290))

App().run()

