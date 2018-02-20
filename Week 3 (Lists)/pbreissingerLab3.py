# Peter Breissinger
# CSCI 1300
# Lab quiz 3

from cs1graphics import *
paper = Canvas(300,300)
width = 50
height = 25

colors = ["blue","green","red"]
coords = [50,200,100,200,150,200,50,225,100,225,150,225]

#First square/topRow
rect1 = Rectangle(width,height,Point(coords[0],coords[1]))
rect1.setFillColor(colors[0])
paper.add(rect1)

#Second sqaure/topRow
rect2 = Rectangle(width,height,Point(coords[2],coords[3]))
rect2.setFillColor(colors[1])
paper.add(rect2)

#Thirds square/topRow
rect3 = Rectangle(width,height,Point(coords[4],coords[5]))
rect3.setFillColor(colors[2])
paper.add(rect3)

#First square/botRow
rect4 = Rectangle(width,height,Point(coords[6],coords[7]))
rect4.setFillColor(colors[2])
paper.add(rect4)

#Second square/botRow
rect5 = Rectangle(width,height,Point(coords[8],coords[9]))
rect5.setFillColor(colors[0])
paper.add(rect5)

#Third square/botRow
rect6 = Rectangle(width,height,Point(coords[10],coords[11]))
rect6.setFillColor(colors[1])
paper.add(rect6)

