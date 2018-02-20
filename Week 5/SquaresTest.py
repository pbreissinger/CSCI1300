from cs1graphics import *
Toggle = True
xaxis = 30
yaxis = 40
dy = 10
width = 10
height = 10
screen = Canvas(500,500)
NumRect = int(raw_input("How many checkboards would you like? "))
rows = raw_input("Enter number of rows: ")
rows = int(rows)
cols = raw_input("Enter number of cols: ")
cols = int(cols)
number = int(raw_input("How many colors would you like to use? "))
i = 0
colors = list()

while i < number:
    x = raw_input("Enter color: ")
    colors.append(x)
    i+=1            

colornum = 0
j = 0
check = 0
f =  0
for j in range (NumRect):
    for i in range (rows):
        dx = 10
        if check >0:
            dx = 10*(cols+f)
        for j in range (cols):
            if colornum == number:
                colornum = 0
            rect = Rectangle(width,height)
            rect.moveTo(xaxis+dx,dy)
            screen.add(rect)
            rect.setFillColor('white')
            if Toggle == True:
                rect.setFillColor('white')
            else:
                rect.setFillColor(colors[colornum])
            Toggle = not Toggle
            dx = dx+width
        dy +=10
        if dy >30:
            dy = 10
            check = 1
            f +=cols
        if cols%2==0:
            Toggle = not Toggle
        else:
            Toggle = Toggle

    colornum +=1
