import pickle
print("\t\t\t\t\t\t\tWelcome to holiday chooser!")
holiday=""
rw=input("Would you like to look at a presaved trip or create a new one (new or existing)?")
amountdef = open("holidaynumber.dat", "rb+")
amount = pickle.load(amountdef)
amountdef.close()
if rw=='new':
    holiday=input("Where will you be going?")
    file = open(holiday+".dat", "wb")
    prosnum=int(input("How many pros are there?"))
    consnum=int(input("How many cons are there?"))
    pickle.dump(prosnum, file)
    pickle.dump(consnum, file)
    pros[""]
    cons[""]
    pros.append(input("What is your first pro?")
    for i in prosnum - 2:
        pros.append(input("What is your next pro?")
    pros.append(input("What is your final pro?")
    cons.append(input("What is your first con?")
    for j in consnum-2:
        cons.append(input("What is your next con?")
    cons.append(input("What is your final con?")
    conimportance=[""]
    proimportance=[""]
    proimportance.append(input("What is the importance of your first pro?")
    for k in prosnum-2:
        proimportance.append(input("What is the importance of your next pro?")
    proimportance.append(input("What is the importance of your final pro?")
    conimportance.append(input("What is the importance of your first con?")
    for g in consnum-2:
        conimportance.append(input("What is the importance of your next con?")
    conimportance.append(input("What is the importance of your final con?")
    print("Your pros:")
    for f in pros:
        print(f)
    print("Your cons:")
    for h in cons:
        print(h)
    
    
    

