# recieve all input as a string and then deal with contents of the string
'''
x = raw_input("Enter a number ")

y = raw_input("Enter another number ")

# Checks if input is a digit, if not it assigns a value of 0
if x.isdigit():
    x = int(x)
else:
    x = 0
if y.isdigit():
    y = int(y)
else:
    y = 0

sum = x+y
print sum
'''


# Recieve string use .split() to get a list
x = raw_input("Enter two numbers separated by a space ")
TheList = x.split()
x = int(TheList[0])
print
'''
if x.isdigit():
    x = int(x)
else:
    x = 0
if y.isdigit():
    y = int(y)
else:
    y = 0

sum = x+y
print sum
'''
