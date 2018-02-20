'''
Name: Peter Breissinger
Email: pbreissinger@gmail.com
Current Date: January 24, 2018
Course Information: CSCI 1300
Instructor: Judy Etchison
'''

# This program will illustrate a fish bowl with a fish blowing bubbles

#Calling cs1graphics
from cs1graphics import *

#Calling sleep function
from time import sleep

#Creating the Canvas titled 'Fish Bowl'
paper = Canvas(500,500,'lightgreen','Fish Bowl')

#Creating a close canvas button
message = Text('Click canvas to close', 20, Point(250,475))
paper.add(message)

#Creating Fish Jar/Bowl
Bowl = Circle(200)
Bowl.setFillColor('skyblue')
Bowl.move(250,250)
Bowl.setDepth(100)
paper.add(Bowl)
BowlTop = Polygon(Point(100,15),Point(400,15),Point(300,57),Point(200,57))
BowlTop.setDepth(2)
BowlTop.setFillColor('white')
paper.add(BowlTop)

#Creating the Fish
body = Circle(30)
body.move(250,250)
body.setFillColor('orange')
paper.add(body)


#Fish eye
eye = Circle(3)
eye.move(235,240)
eye.setFillColor('black')
paper.add(eye)

#Fish tail
tail=Polygon(Point(275,265),Point(280,290),Point(295,255))
tail.setFillColor('orange')
paper.add(tail)

#Creating the rocks/ground
rock = Circle(10)
rock.move(250,425)
rock.setFillColor('grey')
paper.add(rock)

rock2 = Circle(10)
rock2.move(245,440)
rock2.setFillColor('grey')
paper.add(rock2)

rock3 = Circle(10)
rock3.move(265,440)
rock3.setFillColor('grey')
paper.add(rock3)

rock4 = Circle(10)
rock4.move(285,435)
rock4.setFillColor('grey')
paper.add(rock4)

rock5 = Circle(10)
rock5.move(305,432)
rock5.setFillColor('grey')
paper.add(rock5)

rock6 = Circle(10)
rock6.move(325,425)
rock6.setFillColor('grey')
paper.add(rock6)

rock7 = Circle(10)
rock7.move(310,420)
rock7.setFillColor('grey')
paper.add(rock7)

rock8 = Circle(10)
rock8.move(295,415)
rock8.setFillColor('grey')
paper.add(rock8)

rock9 = Circle(10)
rock9.move(275,423)
rock9.setFillColor('grey')
paper.add(rock9)

rock10 = Circle(10)
rock10.move(227,438)
rock10.setFillColor('grey')
paper.add(rock10)

rock11 = Circle(10)
rock11.move(208,435)
rock11.setFillColor('grey')
paper.add(rock11)

rock12 = Circle(10)
rock12.move(190,427)
rock12.setFillColor('grey')
paper.add(rock12)

rock13 = Circle(10)
rock13.move(220,418)
rock13.setFillColor('grey')
paper.add(rock13)


sleep(1)

#Implement 'for' loop so that the animation of the bubbles plays twice through
x=1
for x in range(0,2):

    #Creating bubble 1
    bubble = Circle(6)
    bubble.move(200,200)
    bubble.setFillColor('white')
    paper.add(bubble)
    x +=1


    sleep(1)
    bubble.setFillColor('skyblue')
    bubble.setBorderColor('skyblue')

    #Creating bubble 2
    bubble2 = Circle(6)
    bubble2.move(185,165)
    bubble2.setFillColor('white')
    paper.add(bubble2)
    x+=1


    sleep(1)
    bubble2.setFillColor('skyblue')
    bubble2.setBorderColor('skyblue')

    #Creating bubble 3
    bubble3 = Circle(6)
    bubble3.move(225,155)
    bubble3.setFillColor('white')
    paper.add(bubble3)
    x+=1

    sleep(1)
    bubble3.setFillColor('skyblue')
    bubble3.setBorderColor('skyblue')

    #Creating bubble 4
    bubble4 = Circle(6)
    bubble4.move(175,125)
    bubble4.setFillColor('white')
    paper.add(bubble4)
    x+=1

    sleep(1)
    bubble4.setFillColor('skyblue')
    bubble4.setBorderColor('skyblue')

    #Creating bubble 5
    bubble5 = Circle(6)
    bubble5.move(200,100)
    bubble5.setFillColor('white')
    paper.add(bubble5)
    x+=1

    sleep(1)
    bubble5.setFillColor('skyblue')
    bubble5.setBorderColor('skyblue')

    #Creating bubble 6
    bubble6 = Circle(6)
    bubble6.move(225,70)
    bubble6.setFillColor('white')
    paper.add(bubble6)
    x+=1

    sleep(1)
    bubble6.setFillColor('skyblue')
    bubble6.setBorderColor('skyblue')

paper.wait()
paper.close()


