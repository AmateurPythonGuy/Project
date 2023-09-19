import mysql.connector as mys
import adminFunctions as af
import userFunctions as uf


def connection() -> bool:
    try:
        db = mys.connect(host="localhost", user='root', passwd="root", database="project")
        c = db.cursor()
        return True
    except:
        return False


def login() -> int:
    user = input("Enter username: ")
    passwd = input("Enter password: ")

    if user == "admin" and passwd == "root":
        print("Welcome admin!")
        return 1
    else:
        print("Welcome user!")
        return 0

def userFunctions(funcNum):
    uf.Main.start()
    if funcNum == 0:
        quit()
    elif funcNum == 1:
        while True:
            print("-="*10,"ITEMS(USER)","=-"*10)

            print("[ITEM ID, NAME, QTY, PRICE]")
            uf.Items.viewTable()

            print("1. Place an order \n2. Search for an item \n0. Go back")
            func1 = int(input("Enter function: "))
            
            if func1 == 1:
                uf.Items.order()
                print("Item(s) added to cart")
            elif func1 == 2:
                uf.Items.search()
            elif func1 == 0:
                uf.Main.end()
                break
    elif funcNum == 2:
        while True:
            print("-="*10,"CART","=-"*10)
            uf.Cart.viewTable()

            print("1. Confirm Order \n0. Go back")
            func2 = int(input("Enter function: "))

            if func2 == 1:
                uf.Cart.confirm()
                print("Order confirmed!")
            elif func2 == 0:
                uf.Main.end()
                break
    elif funcNum == 3:
        while True:
            print("-="*10,"DELIVERY","=-"*10)

            print("1. Check delivery status \n0. Go back")
            func3 = int(input("Enter function: "))

            if func3 == 1:
                uf.deliveryStatus()
            elif func3 == 0:
                uf.Main.end()
                break

def adminFunctions(funcNum):
    af.Main.start()
    if funcNum == 0:
        quit()
    elif funcNum == 1:
        while True:
            print("-="*10,"ITEMS(ADMIN)","=-"*10)
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
            print("-="*10,"CUSTOMERS(ADMIN)","=-"*10)
            print("1. View all customers \n2. Add customer\n3. Remove a customer \n4. Search for a customer \n0. Go back")
            func2 = int(input("Enter function: "))

            if func2 == 1:
                af.Customers.viewTable()
            elif func2 == 2:
                af.Customers.addCustomer()
            elif func2 == 3:
                af.Customers.removeCustomer()
            elif func2 == 4:
                af.Customers.searchCustomer()
            elif func2 == 0:
                af.Main.end()
                break
    elif funcNum == 3:
        while True:
            print("-="*10,"TRANSACTIONS(ADMIN)","=-"*10)
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
            print("-="*10,"DELIVERIES(ADMIN)","=-"*10)
            print("1. Check deliveries \n2. Search a delivery\n3. Update delivery status \n0. Go back")
            func4 = int(input("Enter function: "))

            if func4 == 1:
                af.Deliveries.viewTable()
            elif func4 == 2:
                af.Deliveries.search()
            elif func4 == 3:
                af.Deliveries.updateStatus()
            elif func4 == 0:
                af.Main.end()
                break
