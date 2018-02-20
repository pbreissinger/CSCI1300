# 5.28 pg 199
'''
def threshold(dailyGains, goal):
    i = 0
    sum = 0
    while i<len(dailyGains):
        sum = sum+dailyGains[i]
        if sum >= goal:
            return i+1
        i = i+1
    return 0
    # main code____________________________
stocks = [19,49,30,20,10]
result = threshold(stocks,100)
if result == 0:
    print "you cannot reach your goal"
else:
    print ""
'''

'''
def FirstFunction(num1, string1, string2):
    if num1 == 1:
        return string1
    else:
        if x== 2:
            return string1 + string2
        else:
            return
Answer = FirstFunction(3,"hello","goodbye")
print Answer
print FirstFucntion(1,"goodbye","hello")
print FirstFunction(2,"xxx","yyy")
'''

