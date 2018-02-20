from cs1graphics import *

paper = Canvas(300,300)
radius = 30
dx=10

colors = ["red","green","blue"]
coords = [100,200,150,200,200,200]

#Build first circle
circle1 = Circle(radius,Point(coords[0],coords[1]))
circle1.setFillColor(colors[0])

#Build second circle
circle2 = Circle(radius,Point(coords[2]+dx,coords[3]))
circle2.setFillColor(colors[1])

#Build third circle
circle3 = Circle(radius,Point(coords[4]+dx*2,coords[5]))
circle3.setFillColor(colors[2])

#Add circle to canvas
paper.add(circle1)
paper.add(circle2)
paper.add(circle3)
paper.wait()
paper.close()
