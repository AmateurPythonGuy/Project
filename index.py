import mainFunctions as main

if main.connection():
    print("*"*15,"CONNECTED","*"*15)

user = main.login() # 0 = user | 1 = admin

print("-+"*10,"WELCOME TO AMAZON'T","+-"*10,"\n\n")

if user == 1: # admin
    while True:
        print("-$"*15,"ADMIN FUNCTIONS","$-"*15)
        print("1. View/Alter items \n2. Customers \n3. Transactions \n4. Delivery status \n0. Quit")

        func = int(input("Enter function: "))
        main.adminFunctions(func)

elif user == 0: # user
    while True:
        print("&="*15,"USER FUNCTIONS","=&"*15)
        print("1. View items \n2. View Cart \n3. Delivery status \n0. Quit")

        func = int(input("Enter function: "))
        main.userFunctions(func)
