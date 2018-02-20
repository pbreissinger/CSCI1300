'''
def FirstFunction(num):
    string1 = raw_input("Enter a sentence: ")
    string2 = raw_input("Enter another sentence: ")
    if  num == 1:
        print string1
    if num == 2:
        print string1+ string2

    else:
        print ""
'''

def factorial(k):
    if k ==0:
        return 1
    else:
        return k*factorial(k-1)
