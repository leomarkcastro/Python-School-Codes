'''
    Code #2
    Goal:
        Get two digits and put in their respective variable.
        If both are even, add them.
        If both are odd, subtract them.
        If neither, multiply them.

'''

while True:
    try:
        value1 = int(raw_input("Enter your 1st number: "))
        value2 = int(raw_input("Enter your 2nd number: "))

        if (value1%2 == 0) and (value2%2 == 0):
            value3 = value1 + value2
        elif (value1%2 == 1) and (value2%2 == 1):
            value3 = value1 - value2
        else:
            value3 = value1 * value2

        print value3
    except:
        print "Wrong Input"

    if raw_input("\nDo you want to try again?<yes/no>: ").strip().lower() == 'no':
        break
    print

    
