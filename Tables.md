# Tables
All the tables used in this project
### ITEMS

`create table ITEMS (ITEM_ID int primary key, ITEM_NAME varchar(45), QUANTITY int, PRICE int, DOM date);`

```txt
desc items;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| ITEM_ID   | int(11)     | NO   | PRI | NULL    |       |
| ITEM_NAME | varchar(45) | YES  |     | NULL    |       |
| QUANTITY  | int(11)     | YES  |     | NULL    |       |
| PRICE     | int(11)     | YES  |     | NULL    |       |
| DOM       | date        | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
5 rows in set (0.06 sec)
```


### CART

`create table CART (TRANSACTION_ID int primary key, C_ID int, ITEM_ID int, ITEM_NAME varchar(45) ,PRICE int);`

```txt
desc cart;
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| TRANSACTION_ID | int(11)     | NO   | PRI | NULL    |       |
| C_ID           | int(11)     | YES  |     | NULL    |       |
| ITEM_ID        | int(11)     | YES  |     | NULL    |       |
| ITEM_NAME      | varchar(45) | YES  |     | NULL    |       |
| PRICE          | int(11)     | YES  |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+
5 rows in set (0.02 sec)
```


### CUSTOMERS

`create table CUSTOMERS (C_ID int primary key, NAME varchar(25), PHONE_NO int(10), EMAIL varchar(55));`

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
4 rows in set (0.03 sec)
```


### TRANSACTIONS

`create table TRANSACTIONS (T_ID int primary key, C_ID int, MODE_OF_PAYMENT varchar(25), STATUS varchar(5));`

```txt
desc transactions;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| T_ID            | int(11)     | NO   | PRI | NULL    |       |
| C_ID            | int(11)     | YES  |     | NULL    |       |
| MODE_OF_PAYMENT | varchar(25) | YES  |     | NULL    |       |
| STATUS          | varchar(5)  | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
4 rows in set (0.03 sec)
```


### DELIVERY

`create table DELIVERY (E_ID int primary key, T_ID int, DESTINATION varchar(70), STATUS varchar(5));`

```txt
desc delivery;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| E_ID        | int(11)     | NO   | PRI | NULL    |       |
| T_ID        | int(11)     | YES  |     | NULL    |       |
| DESTINATION | varchar(70) | YES  |     | NULL    |       |
| STATUS      | varchar(5)  | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
4 rows in set (0.03 sec)
```
