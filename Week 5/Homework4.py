'''
Homework 4
2/11/2018
'''


#NUMBER 1
'''
total = 0
for k in range (4):
    total +=k/2

print total
'''


#NUMBER 2
'''
from cs1graphics import *
paper  = Canvas(500,500)
colors  = ["red","blue","purple","green","yellow"]
coords = (100,200)
radius = 60
x = 4

for k in range(5):
    target = Circle(radius)
    target.move(250,250)
    paper.add(target)
    target.setFillColor(colors[x])
    radius -=10
    x -= 1
    k+=1
'''


#NUMBER 3
'''
sentence = raw_input("Enter a sentence: ")
sentence.lower()
words = sentence.split()
words.sort()
for word in words:
    print (word)
'''


#NUMBER 4
'''
mystery = raw_input("Enter a sentence: ").lower().strip()
vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvxyz")
NumberVowels = sum(mystery.count(v) for v in vowels)
NumberConsonants = sum(mystery.count(v) for v in consonants)
NVString = str(NumberVowels)
NCString = str(NumberConsonants)
prompt1 = ("There are ")
prompt2 = (" vowels in the string ")
prompt3 = (" consonants in the string ")

print ( prompt1 + NVString+ "" +prompt2+mystery)
print ( prompt1 + NCString+ "" +prompt3+mystery)
'''


#NUMBER 5
'''
scores = raw_input("Enter two test scores: ")
ScoresList = list(map(int, scores.split()))
if ScoresList[0] > ScoresList[1]:
    print ScoresList[0]
else:
    print ScoresList[1]
'''


#NUMBER 6
'''
x = int(raw_input('Enter a value for x: '))
y = int(raw_input('Enter a value or y: '))
if y>=7:
    print 'answer is A'
elif x<4:
    if y>4:
        print 'answer is B'
    else:
        print 'answer is C'
else:
    print 'answer is C'
''' 


#NUMBER 7
'''
checking = raw_input("What is the checking balance? ")
if checking.isdigit():
    checking = int(checking)
else:
    checking = 0
    
saving = raw_input("What is the savings balance? ")
if saving.isdigit():
    saving = int(saving)
else:
    saving = 0
    
charge = .15

if checking >= 1000:
    print ("The charge is $0")
elif saving >= 1500:
    charge = 0
    print ("The charge is $0")
else:
    print ("The charge is $0.15")
'''


#NUMBER 8
'''
item = raw_input("Enter the item: ")
price = raw_input("Enter the price: ")
if price.isdigit():
    price = int(price)
else:
    price = 0
delivery = int(raw_input("Would you like overnight delivery (0 for no, 1 for yes)? "))

shipping  = 0

if delivery == 0:
    if price < 10:
        shipping = 2
    else:
        shipping = 3
else:
    if price < 10:
        shipping = 7
    else:
        shipping = 8

itemString  = str(item)
priceString = str(price)
shipString = str(shipping)
print ("Invoice: ")
print ("     "+itemString + "     " + priceString)
print ("     "+"Shipping" + "  " + shipString)
'''



    
