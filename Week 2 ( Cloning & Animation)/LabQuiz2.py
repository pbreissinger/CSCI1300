'''
Name: Peter Breissinger
Email: pbreissinger@gmail.com
Date: January 25, 2018
Course: CSCI 1300
Instructor: Judy Etchison
'''

from cs1graphics import *

#Creating Cavnas
paper = Canvas(500,500,'skyblue','Snowman World')

#Constructing the Snowman
bottom = Circle(50)
bottom.setFillColor('white')
bottom.move(250,350)
paper.add(bottom)
top = Circle(40)
top.setFillColor('white')
top.move(250,260)
paper.add(top)

#Constructing arms
LeftArm = Path(Point(215,325),Point(195,300))
paper.add(LeftArm)
RightArm = Path(Point(285,325), Point(300,300))
paper.add(RightArm)

#Constructing eyes
LeftEye =  Circle(5)
LeftEye.setFillColor('black')
LeftEye.move(240,245)
paper.add(LeftEye)
RightEye = Circle(5)
RightEye.setFillColor('black')
RightEye.move(260,245)
paper.add(RightEye)

#Constructing the nose
nose = Polygon(Point(250,255),Point(280,260),Point(250,265))
nose.setFillColor('orange')
nose.setDepth(3)
paper.add(nose)

#Constructing the hat
hat = Polygon(Point(240,225),Point(270,225),Point(270,205),Point(260,205),Point(260,190),Point(250,190),Point(250,205),Point(240,205))
hat.setFillColor('black')
paper.add(hat)

#Constructing the smile
smile = Path(Point(240,285),Point(250,295),Point(260,285))
paper.add(smile)

#Adding Message at Bottom
message = Text('Click on snowman to make him frown!',20,Point(250,450))
paper.add(message)

#Adding frown changer
paper.wait()
smile.flip(270)

paper.wait()
paper.close()












