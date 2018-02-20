from cs1graphics import *
paper = Canvas(300,200,'lightblue', 'My World')

head = Circle(11)
paper.add(head)
head.move(100,100)
head.setFillColor('white')
head.setDepth(1)

BackBone = Path(Point(100,110), Point(100,160))        
paper.add(BackBone)

arms = Path(Point(75,112),Point(100,135),Point(125,112))
paper.add(arms)

legs = Path(Point(75,190),Point(100,160),Point(125,190))
paper.add(legs)

grass = Rectangle (800,50)
grass.move(10,200)
grass.setFillColor('green')
grass.setDepth(75)
paper.add(grass)

sun = Circle(30)
paper.add(sun)
sun.setFillColor('yellow')
sun.setBorderColor('yellow')

tree = Polygon(Point(200,165),Point(225,75),Point(250,165))
tree.setFillColor('darkgreen')
paper.add(tree)
trunk = Rectangle(10,20)
trunk.setFillColor('brown')
paper.add(trunk)
trunk.move(225,175)

person = Layer()
person.add(head)
person.add(BackBone)
person.add(legs)
person.add(arms)
paper.add(person)

person2 = person.clone()
person2.scale(.75)
person2.move(100,40)
paper.add(person2)

person3 = person.clone()
person3.scale(.50)
person3.move(5,90)
paper.add(person3)



               
