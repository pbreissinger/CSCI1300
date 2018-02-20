groceries = list()
groceries.append('bread')
apples = 'apples'
groceries.append(apples)
groceries.append(apples)
groceries.append(apples)
groceries.append('milk')
groceries.append(apples)
x=groceries.count('apples')
print x
print groceries

print "the count of the number of apples string is", groceries.count('apples')

#Comma adds the next print statement to the same line as the above
print "Judy","Jane","John", #<------ This comma adds 'Tim' to the same line
print "Tim"

#Removes last element
groceries.pop()
print groceries.append('ice cream') #<---- Does not return a value aka 'none'
groceries.reverse()
print groceries
print groceries.reverse() #<---- Does not return value


