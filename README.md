# Project
MySQL-ing with python

Description: 

A new "online shopping web application" type of application, called 'Amazon't' has entered the market. How will Jeff Bezos keep his business alive anymore? (;-;)  

## Credits
Abhinav - Documentation

Woitiwe(me) - Programming/Coding

George - Debugging/testing

### UPDATE: Documentation added as a seperate file

# Tables
All the tables used in this project

**Tables are in a database named "project"**
### ITEMS

```txt
desc items;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| ITEM_ID   | int(11)     | NO   | PRI | NULL    |       |
| ITEM_NAME | varchar(45) | YES  |     | NULL    |       |
| QUANTITY  | int(11)     | YES  |     | NULL    |       |
| PRICE     | int(11)     | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
4 rows in set (0.07 sec)
```

### CART

```txt
desc cart;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| C_ID  | int(11)     | YES  |     | NULL    |       |
| I_ID  | int(11)     | YES  |     | NULL    |       |
| Name  | varchar(45) | YES  |     | NULL    |       |
| Qty   | int(11)     | YES  |     | NULL    |       |
| Price | int(11)     | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
5 rows in set (0.13 sec)
```


### CUSTOMERS

```txt
desc customers;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| C_ID     | int(11)     | NO   | PRI | NULL    |       |
| NAME     | varchar(25) | YES  |     | NULL    |       |
| PHONE_NO | int(10)     | YES  |     | NULL    |       |
| EMAIL    | varchar(55) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
4 rows in set (0.59 sec)
```


### TRANSACTIONS

```txt
desc transactions;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| T_ID            | int(11)     | NO   | PRI | NULL    |       |
| C_ID            | int(11)     | YES  |     | NULL    |       |
| MODE_OF_PAYMENT | varchar(25) | YES  |     | NULL    |       |
| status          | tinyint(1)  | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
4 rows in set (0.09 sec)
```


### DELIVERIES

```txt
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| T_ID        | int(11)     | NO   | PRI | NULL    |       |
| DESTINATION | varchar(75) | YES  |     | NULL    |       |
| STATUS      | tinyint(1)  | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
3 rows in set (0.14 sec)
```
