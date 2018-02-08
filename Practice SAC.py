#defining x for the while loops
x = 0

while x == 0:
#finding the users gender
    r = input("Male or female? (M or F): ")
#attributing the correct value to 'r'
    if r == "M":
        r = 0.68
        x = 1
    elif r == "F":
        r = 0.55
        x = 1
#correcting any typing error the user may have done
    else:
        print("That is not an option, please enter M or F.")

while x == 1:
#finding the users weight
    W = input("What is your mass/weight in kg?: ")
#testing for typing errors
    try:
        W = float(W)
        if W >= 1:
            x = 2
#correcting any typing error the user may have done
        else:
            print("You must enter a positive value.")
    except:
        print("You must enter an integer.")

while x == 2:
#finding how long since the user had alcohol
    t = input("How long ago since you consumed the alcohol? (hours) ")

    try:
        t = float(t)
        if t >= 0:
            x = 3
# correcting any typing error the user may have done
        else:
            print("You must enter a positive value.")
    except:
        print("You must enter an integer.")

while x == 3:
#finding how many standard drinks the user has had
    A = input("How many standard drinks have you consumed? ")

    try:
        A = float(A)
        if A >= 0:
            x = 4
# correcting any typing error the user may have done
        else:
            print("You must enter a positive value.")
    except:
        print("You must enter an integer.")
#calculating the BAC if the user
BAC = (((A/(r*W))*100)-0.00015*t)/100
#printing BAC of the user
print("Your BAC is:", str("%.2f" % BAC))

while x == 4:
#finding the drivers license of the user
    l = input("Drivers license? (L, P or FL (fully licensed)): ")
    if l == "L":
#printing possible consequences
        if BAC >= 0.5:
            print('''If you drive with this BAC you have your licence 
cancelled for three months and will be required to install 
an alcohol interlock for at least six months once you are relicensed. ''')
        else:
            print("You are safe to drive.")
        x = 5
    elif l == "P":
        if BAC >= 0.5:
            print('''If you drive with this BAC you will have your licence 
cancelled for three months and will be required to install an alcohol 
interlock for at least six months once you are relicensed. ''')
        else:
            print("You are safe to drive.")
        x = 5
    elif l == "FL":
        if BAC >= 0.5 and BAC < 0.7:
            print('''If you drive with this BAC you will be fined and incur 10 demerit points.''')
        if BAC >= 0.7:
            print('''If you drive with this BAC you will have your licence 
cancelled and be required to install an alcohol interlock 
for at least six months once you are relicensed.''')
        else:
            print("You are safe to drive.")
        x = 5
# correcting any typing error the user may have done
    else:
        print("That is not an option, please enter L, P or FL.")
#exiting program
exit(0)