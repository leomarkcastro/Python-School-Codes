'''
    Code #1
    Goal:
        Use raw_input() to get two separate values to be put in their respective variables.
        With these two inputs, compute them three times with any distinct operator methods (+-/*)
'''

while True:

    try:
        value1 = int(raw_input("Input your 1st number: "))
        value2 = int(raw_input("Input your 2nd number: "))

        print value1,'*',value2,'=',(value1*value2)
        print value1,'+',value2,'=',(value1+value2)
        print value1,'-',value2,'=',(value1-value2)
        
        print value1,'>=',value2,'=',(value1>=value2)
        print value1,'<=',value2,'=',(value1<=value2)
        print value1,'==',value2,'=',(value1==value2)
        
        print value1,'^',value2,'=',(value1^value2)
        print value1,'&',value2,'=',(value1&value2)
        print value1,'|',value2,'=',(value1|value2)

        value3 = value1
        value1+=value2; print value3,'+=',value2,'=',(value1)
        value1 = value3
        value1-=value2; print value3,'-=',value2,'=',(value1)
        value1 = value3
        value1*=value2;print value3,'*=',value2,'=',(value1)
    except:
        print "Wrong input"

    if raw_input("\nDo you want to try again?<yes/no>: ").strip().lower() == 'no':
        break
    print

