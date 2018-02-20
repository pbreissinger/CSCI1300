from cs1graphics import *
paper = Canvas(500,500)

num = raw_input("How many rectangles do you want? ")
if num.isdigit():
    num = int(num)
else:
    num = 0
    
color1 = raw_input("Enter the color you want to use: ")
color2 = raw_input("Enter another favorite color to use: ")
colors = []
colors.append(color1)
colors.append(color2)

x=0

toggle = True
for i in range (num):
    rect = Rectangle(20,20)
    paper.add(rect)
    rect.move(20 + x,20)
    if toggle == True:
        rect.setFillColor(colors[0])
    else:
        rect.setFillColor(colors[1])
    toggle = not toggle
    x+=20
paper.wait()
paper.close()
