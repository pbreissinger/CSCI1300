# Prelab 5
while True:
    romanNumber = raw_input("Enter an integer from 1-9: ")
    if romanNumber.isdigit():
        romanNumber = int(romanNumber)

    x = romanNumber
    for x in range(1,8):
        if romanNumber == 0:
            print ''
        elif romanNumber == 1:
            print ('1 as a roman numeral is I')
            break
        elif romanNumber == 2:
            print('2 as a roman numeral is II')
            break
        elif romanNumber == 3:
            print('3 as a roman numeral is III')
            break
        elif romanNumber == 4:
            print('4  as a roman numeral is IV')
            break
        elif romanNumber == 5:
            print('5 as a roman numeral is V')
            break
        elif romanNumber == 6:
            print('6 as a roman numeral is VI')
            break
        elif romanNumber == 7:
            print('7 as a roman nuumeral is VII')
            break
        elif romanNumber == 8:
            print('8 as a roman numeral is VIII')
            break
        elif romanNumber == 9:
            print ('9 as a roman numeral is IX')
            break
        if romanNumber > 9:
            raise ValueError("10 cannot be put into this program")

    while True:
        answer = raw_input('Run again? (y/-1): ')
        if answer in ('y','-1'):
            break
        print 'Invalid input'
    if answer == 'y':
        continue
    else:
        print 'Goodbye'
        break
    
