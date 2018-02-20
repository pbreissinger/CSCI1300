'''
Peter Breissinger
February 2, 2018
Judy Etchison
Homework3
'''

# Question 1
'''
Hours = int(raw_input('How many hours did you work? '))
Pay = int(raw_input('How much do you get paid per hour? '))
GrossPay = Hours * Pay
print 'Your total gross pay is',GrossPay
'''

# Question 2
Friends = ['Peter','Bridget','Jack']
print Friends
Friends.sort()
print Friends
print Friends[1]

#Question 3
Vowelstring = " ".join(Friends)
Vowelstring.lower()
a = int(Vowelstring.count('a'))
e = int(Vowelstring.count('e'))
i = int(Vowelstring.count('i'))
o = int(Vowelstring.count('o'))
u = int(Vowelstring.count('u'))
total = a+e+i+o+u
print total

#Question 4
Friends = range(15,38,3)
print Friends[3]

#Question 5
value = list()
value = [1,2,3,4]
print sum(value)/len(value)


#Question 6
s = "example"
s = s[0:5]
print s
#examp



