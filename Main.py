import mysql.connector as mys
import Functions as f
from random import randint

db = mys.connect(host="localhost", user='root', passwd="root", database="project")
c = db.cursor()

class Login:
    def userLogin():
        global ciD
        ciD = randint(200, 299)

        name = input("Enter name: ")
        email = input("Enter email address: ")

        while True:
            phno = int(input("Enter phone number: "))
            if len(str(phno)) > 10:
                print("Invalid phone number. Try again")
                continue
            break

        c.execute(f"insert into customers values ({ciD},'{name}',{phno},'{email}')")
        db.commit()

        print(f"Your Customer ID is {ciD}")
    
    def check(C_ID):
        c.execute("select * from customers")
        table = c.fetchall()

        for i in table:
            if C_ID in i:
                print(f"Hiya {i[1]}!")
                return True
        else:
            return False

    def login():
        print("(Login)")
        cID = input("Enter customer ID (leave blank if new user): ")
        if cID == '1': #admin
            return 1
        elif cID == '': # new user
            Login.userLogin()
        else: # existing user
            return cID
    


'''if f.connection():
    print("*"*15,"CONNECTED","*"*15)'''

user = Login.login() # 0 = user | 1 = admin
ciD = user

if user == 1: # admin
    print("Hello Admin!")
    while True:
        print("-$"*15,"ADMIN FUNCTIONS","$-"*15)
        print("1. View/Alter items \n2. Customers \n3. Transactions \n4. Delivery status \n0. Quit")

        func = int(input("Enter function: "))
        f.adminFunctions(func)

else: # user
    if user == 2:
        print("Welcome user! \nPlease Login below")
        Login.userLogin()
    else:
        ciD = int(input("Enter it again: "))

        if Login.check(ciD):
            pass
        else:
            print("Invalid customer ID \nClosing program...")
            quit()
    
    print("-+"*10,"WELCOME TO AMAZON'T","+-"*10,"\n\n")

    while True:
        print("&="*15,"USER","=&"*15)
        print("1. View items \n2. View Cart \n3. Delivery status \n0. Quit")

        func = int(input("Enter function: "))
        f.userFunctions(func)
