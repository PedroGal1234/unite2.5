#Pedro Gallino
#9/20/17
#isreal.py - shows the Isreali flag

from ggame import *

blue = Color(0x000ff,1)
white = Color(0xffffff,1)

blueOutline = LineStyle(10,blue)

rectangle1 = RectangleAsset(100,100,blueOutline,blue)
rectangle2 = RectangleAsset(100,100,blueOutline,blue)
triangle1 = PolygonAsset([(0,50),(75,-50),(150,50)],blueOutline,white)
triangle2 = PolygonAsset([(0,-50),(75,50),(150,-50)],blueOutline,white)

Sprite(rectangle1,(100,100))
Sprite(rectangle2,(200,200))
Sprite(triangle1,(300,300))
Sprite(triangle2,(400,400))

App().run()

