from cs1graphics import *
Canvas()
paper=Canvas(600,400,'skyblue','Christmas tree')
trunk = Rectangle(20,40)
trunk.setFillColor('brown')
paper.add(trunk)
trunk.move(300,300)
tree = Polygon(Point(250,300),Point(300,150),Point(350,300))
tree.setFillColor('darkGreen')
paper.add(tree)
#Implement a widget here
message = Button('Click Me', Point(300,100))
paper.add(message)
message.wait()
paper.close()

