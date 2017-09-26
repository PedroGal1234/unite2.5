#Pedro Gallino
#9/20/17
#isreal.py - shows the Isreali flag

from ggame import *

blue = Color(0x000ff,1)
white = Color(0xffffff,0)

blueOutline = LineStyle(10,blue)

rectangle1 = RectangleAsset(500,100,blueOutline,blue)
rectangle2 = RectangleAsset(500,100,blueOutline,blue)
triangle1 = PolygonAsset([(0,50),(75,-65),(150,50)],blueOutline,white)
triangle2 = PolygonAsset([(0,-50),(75,65),(150,-50)],blueOutline,white)

Sprite(rectangle1,(140,0))
Sprite(rectangle2,(140,310))
Sprite(triangle1,(300,200))
Sprite(triangle2,(300,225))

App().run()

