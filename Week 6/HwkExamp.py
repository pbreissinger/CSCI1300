from cs1graphics import *
def functiontest(b,c):
    screen = Canvas(200,200)
    screen.add(b)
    b.moveTo(100,100)
    c+=5
    b.setFillColor('red')
    print c
    number = 2
    print number
    screen.wait()
    screen.close()
#_______________________________ end of function test


# main code
print number
number = 3
rect = Rectangle (50,20)
rect.setFillColor('green')
circle = Circle(40)
screen.add(circle)
functiontest(rect,number)
print rect.getFillColor()
print number
    
