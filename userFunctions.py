import mysql.connector as mys
from random import randint
from random import choice

addresses = [
    "8939 High Point St.",
    "233 New Saddle St.",
    "9197 Sunbeam Ave.",
    "7800 E. Lake Forest Lane",
    "224 Lower River St.",
    "8603 Bedford Street",
    "94 St Margarets Dr.",
    "688 Buckingham Dr.",
    "378 Beaver Ridge Drive",
    "82 W. Main Circle",
    "423 Birchpond Dr.",
    "636 Westport St.",
    "444 Armstrong St.",
    "50 Essex St.",
    "8876 Hudson Court",
    "19 Spruce Drive",
    "630 Hudson Street",
    "56 East Windsor Street",
    "7799 Queen Street",
    "89 Meadowbrook Rd.",
    "33 Smith Dr.",
    "8271 Fordham Ave.",
    "522 Prince Ave.",
    "5 East Lilac Street",
    "553 Trenton St."
]


class Main:
    def start():
        global db ; global c;
        db = mys.connect(host="localhost", user='root', passwd="root", database="project")
        c = db.cursor()

    def end():
        c.close()
        db.close()


class Items:
    def viewTable():
        c.execute("select * from items;")
        table = c.fetchall()
        for i in table:
            print(i)
            
    def order():
        global ciD
        try:
            ciD = int(input("Enter customer ID: "))
            iD = int(input("Enter item ID: "))
            qty = int(input("Enter quantity required: "))

            c.execute(f"select * from items where ITEM_ID={iD}")
            record = c.fetchone()

            temp = list(record)
            temp[-2] = qty
            temp = [ciD]+temp

            c.execute(f"insert into cart values {tuple(temp)}")
            db.commit()
        except:
            print("ID not found. Try again")
    
    def search():
        iD = int(input("Enter item ID: "))

        c.execute(f"select * from items where ITEM_ID={iD}")
        record = c.fetchone()

        if record is None:
            print("Item not available")
        else:
            print(record)
    

class Cart:
    def viewTable():
        c.execute("select * from cart")
        table = c.fetchall()
        for i in table:
            print(i)
    
    def confirm():
        ciD = int(input("Enter customer ID: "))
        moP = input("Enter mode of payment: (Cash/Credit/UPI): ")

        t_ID = randint(500, 599)
        address = choice(addresses)

        c.execute(f"insert into transactions values ({t_ID},{ciD},'{moP}', 0)")
        c.execute(f"insert into deliveries values ({t_ID},'{address}', 0)")
        c.execute("delete from cart")
        db.commit()

        print("Your transaction ID is:",t_ID)


def deliveryStatus():
    t_ID = int(input("Enter transaction ID: "))
    try:
        c.execute(f"select * from deliveries where T_ID={t_ID}")
        record = c.fetchone()

        if record[-1] == 0:
            print("Order awaiting delivery")
        else:
            print("Order has been delivered")
    except:
        print("Transaction ID not found")
