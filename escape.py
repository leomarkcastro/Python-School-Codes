'''
    Code #3
    Goal:
        Use raw_input() to get integer from user.
        The user must predict the next value if it is odd or even.
        Predict correctly 3x and the program will end

'''

import random

while True:
    score = 0

    print "Win 3 times in a row and you can escape the infinite loop!"

    while (score < 3):

        answer = raw_input("The next value will be <even/odd>: ")

        number = random.randint(0,20000)

        if(number % 2 == 0):
            if answer == 'even':
                score = score + 1
                print "Lucky!"
            else:
                score = 0
                print "Awww. Wrong guess"
                
        elif (number % 2 == 1):
            if answer == 'odd':
                score = score + 1
                print "Lucky!"
            else:
                score = 0
                print "Awww. Wrong guess"

    print "You win!"

    if raw_input("\nDo you want to try again?<yes/no>: ").strip().lower() == 'no':
        break
    print
    
        
