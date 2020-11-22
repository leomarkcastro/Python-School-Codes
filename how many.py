'''
    Code #5
    Goal:
        Perform two input. The first input is a number. This number will be the max length of the second input string.
        Count the alphabet, number and symbols on the second input string.

'''

while True:
    try:
        count = int(raw_input("Enter the number of characters of your sentence: "))

        while(True):
            sentence = raw_input("Enter your sentence: ")
            if (len(sentence) <= count):                                                        
                break                                   
            print 'Your sentence is longer than your count'

        alpha = digit = symbol = 0

        for i in sentence:
            if i.isalpha():
                alpha += 1
            elif i.isdigit():
                digit += 1
            else:
                symbol += 1

        print "\nYour Sentence: ", sentence, "\ncontains:\n"
        print alpha, "letters"
        print digit, "digits"
        print symbol, "symbols"

    except:
        print "Wrong Input"

    if raw_input("\nDo you want to try again?<yes/no>: ").strip().lower() == 'no':
        break
    print


