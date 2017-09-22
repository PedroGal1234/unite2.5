#Pedro Gallino
#9/20.17
#house.py - shows a house

#blueCircle = CircleAsset(50,blackOutline,blue)
#greenEllipse = EllipseAsset(100,50,blackOutline,green)

#Sprite(blueCircle,(700,50))
#Sprite(greenEllipse,(700,200))

from ggame import *

red = Color(0xff0000,1) #(color, transperancy)
green = Color(0x00ff00,1)
blue = Color(0x000ff,1)
black = Color(0x00000,1)
cyan = Color(0xfffff,1)
brown = Color(0x98B4513,1)
silver = Color(0xC0C0C0,1)

blackOutline = LineStyle(2,black) #(pixels, color)

brownDoor = RectangleAsset(80,100,blackOutline,brown)
brownDoor2 = CircleAsset(40,blackOutline,brown)
redRectangle = RectangleAsset(400,300,blackOutline,red)
blackRectangle = RectangleAsset(50,100,blackOutline,black)
silverTriangle = PolygonAsset([(-10,0),(200,-200),(410,0)],blackOutline,silver)
cyanWindow = RectangleAsset(60,70,blackOutline,cyan)

Sprite(redRectangle,(175,250))
Sprite(blackRectangle,(475,100))
Sprite(silverTriangle,(175,250))
Sprite(brownDoor2,(375,430))
Sprite(brownDoor,(335,430))
Sprite(cyanWindow,(440,300))
App().run()