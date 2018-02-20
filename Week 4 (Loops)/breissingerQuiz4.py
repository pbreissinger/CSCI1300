from random import randint

problems = raw_input('How many problems would you like to try today? ')
if  problems.isdigit():
    problems = int(problems)
else:
    problems = 0
    print "Goodbye."
WrongAnswer = 0
CorrectAnswer = 0
WrongAnswer = 0
CorrectAnser = 0

for i in range(problems):
    x = randint(1,10)
    y = randint(1,10)

    StringX = str(x)
    StringY = str(y)

    prompt1 = "What is "
    prompt2 = " plus "
    prompt3 = "? "

    answer = raw_input(prompt1 +StringX+ prompt2+StringY+prompt3)
    if answer.isdigit():
        answer = int(answer)
    else:
        answer = 0

    prompt4 = "Incorrect. The correct answer is "
    correct = x+y

    if answer == correct:
        CorrectAnswer+=1
        print "Correct!"
    else:        
        WrongAnswer +=1
        StringCorrect = str(correct)
        print (prompt4 + StringCorrect)

StringCorrect = str(CorrectAnswer)
StringWrong = str(WrongAnswer)
prompt5 = "You got "
prompt6 = " correct "
prompt7 = "and "
prompt8 = " wrong."
print (prompt5+StringCorrect +prompt6+prompt7+StringWrong +prompt8)


