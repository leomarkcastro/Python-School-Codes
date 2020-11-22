import random

while True:
    a1 = raw_input("(1/4)Enter any value or string: ")
    a2 = raw_input("(2/4)Enter any value or string: ")
    a3 = raw_input("(3/4)Enter any value or string: ")
    a4 = raw_input("(4/4)Enter any value or string: ")

    mytup = (a1,a2,a3,a4); print

    b1 = raw_input("(1/4)Enter any value or string: ")
    b2 = raw_input("(2/4)Enter any value or string: ")
    b3 = raw_input("(3/4)Enter any value or string: ")
    b4 = raw_input("(4/4)Enter any value or string: ")

    mylist = [b1,b2,b3,b4]; print

    mydict = dict()

    for i in range(4):mydict[mytup[i]] = mylist[i]


    ra_in = raw_input("Enter any value or string: ")
            
    if (random.randint(0,100)>50):
        mydict[ ra_in ] = mydict.pop( random.choice(mydict.keys()) )
    else:
        mydict[ random.choice(mydict.keys()) ] = ra_in
    print
    streak = 0      
    while(streak < 3):                                                  
        ra_in = raw_input('Guess my action, <spare or delete>: ')                       
        if (random.randint(0,100)>50):chance = 'spare'
        else:chance = 'delete'       
        if (ra_in == chance):
            print "\nYou win! Here's your rewaard:"
            print mydict; break
        else:
            streak += 1
            if (streak<3): print "Your guess is wrong! "+str(3-streak)+" tries remaining"
    else:
        print "\nAwwww, you guessed wrong three times. Here's an empty dictionary"
        mydict.clear()
        print mydict

    if raw_input("\nDo you want to try again?<yes/no>: ").strip().lower() == 'no':
        break
    print
        



