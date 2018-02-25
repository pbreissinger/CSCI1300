
from random import randint

def random4digi(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
code = random4digi(4)
print code


attempts = 0
exact = 0
close = 0
while attempts <10:
    guess = raw_input('Enter a 4 digit guess: ')
    if guess.isdigit():
        guess = guess
        if len(guess) == 4:
            guess = int(guess)
            def check(guess,code):
                if code == guess:
                    return True
                else:
                    return False
            result = (check(guess,code))
            if result == False:
                attempts +=1
                guess = str(guess)
                code = str(code)
                for i in range(4):
                    if code[i] == guess[i]:
                        exact+=1
                    else:
                        if (guess[i] != code[i]) and (guess[i] in code):
                            close+=1
                if exact == 4:
                    attempts = str(attempts)
                    print ('Success! It took you {} attempts!'.format(''.join(attempts)))
                    break
                else:
                    exact = str(exact)
                    close = str(close)
                    print ('Incorect. {} digits were in the right place and {} were close. Try again.'.format(exact,close))
                    exact = 0
                    close = 0
            else:
                attempts +=1
                attempts = str(attempts)
                print ('Success! It took you {} attempts!'.format(''.join(attempts)))
                break
        else:
            print ('Invalid input. Enter 4 digits.')
    else:
        print ('Invalid input. Enter 4 digits, not characters.')

while attempts == 10:
    code = str(code)
    print ('Game over. The correct code was {}.'.format(''.join(code)))
    break

