from cs1graphics import *
from time import *

paper = Canvas(500,500)

#Body of traffic light
body = Rectangle(100,300)
body.move(250,200)
body.setFillColor('grey')
paper.add(body)
sleep(1)

#Red Light/stop light
stop = Circle(30)
stop.setFillColor('red')
stop.move(250,100)
paper.add(stop)
stop.setDepth(1)
sleep(1)
stop.setFillColor('black')

#Yellow Light/caution light
caution = Circle(30)
caution.setFillColor('yellow')
caution.move(250,200)
paper.add(caution)
caution.setDepth(1)
sleep(1)
caution.setFillColor('black')

#Green Light/go light
go = Circle(30)
go.setFillColor('green')
go.move(250,300)
paper.add(go)
go.setDepth(1)
sleep(1)
go.setFillColor('black')










