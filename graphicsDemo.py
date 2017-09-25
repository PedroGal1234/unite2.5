#Pedro Gallino
#9/20.17
#graphicsDemo.py - intro to graphics using ggam

from ggame import *

red = Color(0xff0000,1) #(color, transperancy)
green = Color(0x00ff00,1)
blue = Color(0x000ff,1)
black = Color(0x00000,1)

blackOutline = LineStyle(10,black) #(pixels, color)

redRectangle = RectangleAsset(100,100,blackOutline,red) #(width, height, outline, fill)
blueCircle = CircleAsset(50,blackOutline,blue) #(radius, outline, fill)
greenEllipse = EllipseAsset(100,50,blackOutline,green) #(Horizontal Radius, Vertical Radius, outline, fill)
blackLine = LineAsset(50,160,blackOutline) #(x endpoint,y endpoint,lineStyle)
redTriangle = PolygonAsset([(0,0),(120,180),(60,300)],blackOutline,red)
text = TextAsset('Pedro', fill=green, style='bold 40pt Times')

Sprite(redRectangle,(175,100))
Sprite(blueCircle,(700,50)) #(number of pixels to the right, Number of pixels down)
Sprite(greenEllipse,(700,200))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text,(300,100))
App().run()
