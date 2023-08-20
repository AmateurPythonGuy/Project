import mysql.connector as mys
import adminFunctions as af


db = mys.connect(host="localhost", user='root', passwd="root", database="project")

def connection() -> bool:
    if db.is_connected():
        return True
    else:
        return False
    

def login() -> int:
    user = input("Enter username: ")
    password = input("Enter password: ")
    if user == "admin" and password == "root":
        print("Welcome admin!")
        return 1; 
    else:
        print("Welcome user!")
        return 0;


def adminFunctions(funcNum):
    af.Main.start()
    if funcNum == 0:
        quit()
    elif funcNum == 1:
        while True:
            print("-="*10,"ITEMS","=-"*10)
            print("1. Add item \n2. Delete item \n3. Search item \n4. View table \n0. Go back")
            func1 = int(input("Enter function: "))

            if func1 == 1:
                af.Items.insertItem()
                print("Item added\n")
            elif func1 == 2:
                af.deleteItem()
                print("Item deleted\n")
            elif func1 == 3:
                af.Items.searchItem()
            elif func1 == 4:
                af.Items.viewTable()
            elif func1 == 0:
                af.Main.end()
                break
            else:
                print("What are you doing here?")

    elif funcNum == 2:
        while True:
            print("-="*10,"CUSTOMERS","=-"*10)
            print("1. View all customers \n2. Remove a customer \n3. Search for a customer \n0. Go back")
            func2 = int(input("Enter function: "))

            if func2 == 1:
                af.Customers.viewTable()
            elif func2 == 2:
                af.Customers.removeCustomer()
            elif func2 == 3:
                af.Customers.searchCustomer()
            elif func2 == 0:
                af.Main.end()
                break
    
    elif funcNum == 3:
        while True:
            print("-="*10,"TRANSACTIONS","=-"*10)
            print("1. View transactions \n2. Update transaction \n3. Check transaction\n0. Go back")
            func3 = int(input("Enter function: "))

            if func3 == 1:
                af.Transactions.viewTable()
            elif func3 == 2:
                af.Transactions.update()
            elif func3 == 3:
                af.Transactions.check()
            elif func3 == 0:
                af.Main.end()
                break
        
    elif funcNum == 4:
        while True:
            print("-="*10,"DELIVERIES","=-"*10)
            print("1. Add a delivery\n2. Check deliveries \n3. Search a delivery\n4. Update delivery status \n5. Cancel a delivery\n0. Go back")
            func4 = int(input("Enter function: "))

            if func4 == 1:
                af.Deliveries.addRecord()
            elif func4 == 2:
                af.Deliveries.viewTable()
            elif func4 == 3:
                af.Deliveries.search()
            elif func4 == 4:
                af.Deliveries.updateStatus()
            elif func4 == 0:
                af.Main.end()
                break


'''
def userFunctions(funcNum):
    pass'''