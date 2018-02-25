while True:
    print '----------MASTERMIND----------'
    from random import randint

    def random4digi(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        if range_start == 0:
            range_start = randint[1,4]
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
                x = 0
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
                    code0 = code
                    guess0 = guess
                    for i in range(len(code)):
                        if code[0] == guess[0]:
                            exact+=1
                            code = code[1:]
                            guess = guess[1:]
                            close -=1
                        else:
                            if (guess[0]!=code[0]) and (guess[0] in code):
                                close+=1
                                code = code[1:]
                                guess = guess[1:]
                        print code
                        print guess
                        if close<0:
                            close=0
                    code = code0
                    guess = guess0
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
    while True:
        answer = raw_input('Run again? (yes/no): ')
        if answer in ('yes','no'):
            break
        print 'Invalid input.'
    if answer == 'no':
        print
        print 'Goodbye'
        break
    else:
        print
        continue            
