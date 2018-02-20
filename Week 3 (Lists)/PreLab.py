'''
Peter Breissinger
CSCI 1030
January 31, 2018
Jud Etchison
'''
from cs1graphics import *
paper = Canvas(600,600)
radius = 30

colors = ["red","blue","yellow","green","purple","black"]
coords = [50,200,100,200,150,200,200,200,250,200,300,200]

#Build first circle
circle1 = Circle(radius,Point(coords[0],coords[1]))
circle1.setFillColor(colors[0])

#Build second circle
circle2 = Circle(radius,Point(coords[2],coords[3]))
circle2.setFillColor(colors[1])

#Build third circle
circle3 = Circle(radius,Point(coords[4],coords[5]))
circle3.setFillColor(colors[2])

#Build fourth circle
circle4 = Circle(radius,Point(coords[6],coords[7]))
circle4.setFillColor(colors[3])

#Build fifth circle
circle5 = Circle(radius,Point(coords[8],coords[9]))
circle5.setFillColor(colors[4])

#Build sixth color
circle6 = Circle(radius,Point(coords[10],coords[11]))
circle6.setFillColor(colors[5])

#Add to canvas
paper.add(circle1)
paper.add(circle2)
paper.add(circle3)
paper.add(circle4)
paper.add(circle5)
paper.add(circle6)
                     
