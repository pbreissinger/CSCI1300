# Peter Breissinger

#4.2
'''
dramatic = ' '
for char in original:
    dramatic +=char+char
'''

#4.4
'''
from cs1graphics import*

numLevels = int(raw_input('How many level wouuld you like? ')) # number of levels
unitSize = 12 # the height of one level
screenSize = unitSize *(numLevels + 1)
paper = Canvas(screenSize, screenSize)
centerX = screenSize / 2.0 # same for all levels

# create levels from top to bottom
for level in range(numLevels):
    width = (level + 1)* unitSize # width varies by level
    block = Rectangle(width, unitSize) # height is always unitSize
    centerY = (level + 1)* unitSize
    block.move(centerX, centerY)
    block.setFillColor('gray')
    paper.add(block)
'''

#4.21
'''
(a) 'D'
(b) 'B'
(c) 'C'
(d) 'B'
'''

#5.3
