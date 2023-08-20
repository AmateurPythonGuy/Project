# Functions

Context {
    This file contains all the functions used in the making of AMAZON'T
}

# main functions
{handles all the broader input}

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






# admin functions
{handles all input specific to admin functions}

{classes to group everything togther nicely}

class Main:
    def start():
        global db ; global c;
        db = mys.connect(host="localhost", user='root', passwd="root", database="project")
        c = db.cursor()


    def end():
        c.close()
        db.close()


# functions related to table 'ITEMS'
class Items:
    def insertItem():
        iD = int(input("Enter item iD: "))
        name = input("Enter item name: ")
        price = int(input("Enter price: "))
        qty = int(input("Enter quantity: "))

        c.execute(f"insert into items values ({iD},'{name}',{price},{qty})")
        db.commit()


    def deleteItem():
        iD = int(input("Enter iD of item to be deleted: "))
        c.execute(f"delete from items where ITEM_ID={iD}")
        db.commit()


    def searchItem():
        iD = int(input("Enter iD of item to be searched: "))
        c.execute(f"select * from items where ITEM_ID={iD}")
        record = c.fetchone()
        print(record)


    def viewTable():
        c.execute("select * from items")
        table = c.fetchall()
        for i in table:
            print(i)


# functions related to table 'CUSTOMERS'
class Customers:
    def viewTable():
        c.execute("select * from customers")
        table = c.fetchall()
        for i in table:
            print(i)


    def removeCustomer():
        iD = input("Enter customer iD: ")
        c.execute(f"delete from customers where C_ID={iD}")
        db.commit()


    def searchCustomer():
        iD = int(input("Enter iD of customer to be searched: "))
        c.execute(f"select * from customers where C_ID={iD}")
        record = c.fetchone()
        print(record)


# functions related to table 'TRANSACTIONS'
class Transactions:
    def viewTable():
        c.execute("select * from transactions")
        table = c.fetchall()
        for i in table:
            print(i)
    

    def update():
        iD = int(input("Enter transaction ID: "))
        value = int(input("Completed/Incomplete (0/1): "))

        c.execute(f"update table transactions set STATUS={value} where T_ID={iD}")
        db.commit()

        print("Updated!")
    

    def check():
        iD = int(input("Enter transaction ID: "))
        c.execute(f"select * from transactions where T_ID={iD}")
        check = c.fetchone()

        if check[-1] == 1:
            print("Transaction completed")
        else:
            print("Transaction incomplete")
