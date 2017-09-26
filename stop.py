#Pedro Gallino
#9/20/17
#stop.py - shows a stop sign


from ggame import *

red = Color(0xff0000,1)
white = Color(0xffffff,1)

redOutline = LineStyle(10,red)

redOctagon = PolygonAsset([(0,0),(50,50),(60,0),(110,0),(],redOutline,red)
text = TextAsset('Stop', fill=white, style='bold 40pt Times')