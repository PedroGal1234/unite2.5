#Pedro Gallino
#9/20.17
#house.py - shows a house


from ggame import *

red = Color(0xff0000,1) #(color, transperancy)
green = Color(0x00ff00,1)
blue = Color(0x000ff,1)
black = Color(0x00000,1)

blackOutline = LineStyle(10,black) #(pixels, color)

redRectangle = RectangleAsset(100,100,blackOutline,red)
blueCircle = CircleAsset(50,blackOutline,blue)
greenEllipse = EllipseAsset(100,50,blackOutline,green)
blackLine = LineAsset(50,160,blackOutline)
redTriangle = PolygonAsset([(0,0),(120,180),(60,300)],blackOutline,red)

Sprite(redRectangle,(175,100))
Sprite(blueCircle,(700,50))
Sprite(greenEllipse,(700,200))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text,(300,200))
App().run()