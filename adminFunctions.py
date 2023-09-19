import mysql.connector as mys

# Common for all admin functions
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
    
    def addCustomer():
        ciD = int(input("Enter customer ID: "))
        name = input("Enter name: ")
        phno = int(input("Enter phone number: "))
        email = input("Enter email address: ")

        c.execute(f"insert into customers values ({ciD},'{name}',{phno},'{email}')")
        db.commit()

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


# functions related to table 'DELIVERY'
class Deliveries:
    def viewTable():
        c.execute("select * from deliveries")
        table = c.fetchall()
        for i in table:
            print(i)
    
    def search():
        iD = int(input("Enter transaction ID: "))
        c.execute(f"select * from deliveries where T_ID={iD}")
        record = c.fetchone()
        print(record)
    
    def updateStatus():
        iD = int(input("Enter transaction ID: "))
        value = int(input("Enter status (0/1): "))

        c.execute(f"update deliveries set status={value} where T_ID={iD}")
        db.commit()

        print("Status updated!")
