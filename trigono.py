'''
    Code #4
    Goal:
        Use raw_input() to get integer from user 3 times.
        Put all these input in a list.
        Do these steps three times:
            Shuffle the list
            Get the first two values from the list
            Use these to get the pythagorean theorem

'''

import random

while True:
    try:
        numbers = [''] * 3

        numbers[0] = int(raw_input("Input your 1st number: "))
        numbers[1] = int(raw_input("Input your 2nd number: "))
        numbers[2] = int(raw_input("Input your 3rd number: "))

        for i in range(3):
            random.shuffle(numbers)

            x = numbers[0]
            y = numbers[1]
            
            print "(" , x , "^ 2 +" , y , "^ 2 )^(0.5) = " , ((x ** 2) + (y ** 2))**(0.5)

    except:
        print "Wrong input"

    if raw_input("\nDo you want to try again?<yes/no>: ").strip().lower() == 'no':
        break
    print
