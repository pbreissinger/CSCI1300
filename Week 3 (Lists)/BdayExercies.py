# .split method
bday = '01/03/70'
date = bday.split('/')
print "My birthday month is ", date[0]
print "My birthday day is ", date[1]
print "My birthday year is ", date[2]


# .join method (returns string)
guests = ['John','Mary','Amy']
conjunction = ' and '
print conjunction.join(guests)


