Some notes regarding this project

# Name: Amazon't (Confirmed)

## Credits:
### Programming - Woitiwe
### Documentation - Abhinav
### Debugging, testing etc - George

###### (Its all me but what the hell?)
## Files:
```txt
1. Main.py: the root file

2. Functions: redirects user to the user and admin mainFunctions

3. adminFunctions: functions related to being an admin. adding items to table, confirming orders etc

4. userFunctions: functions related to being a user. ordering stuff, checking delivery statuses etc
```

## Table details:
All the tables in the program exist in a database called 'project'

create table ITEMS (ITEM_ID int primary key, ITEM_NAME varchar(45), PRICE int);

create table CUSTOMERS (C_ID int primary key, NAME varchar(25), PHONE_NO, int(10), EMAIL varchar(55));

`C_ID is generated randomly`

create table TRANSACTIONS (T_ID int primary key, C_ID int, MODE_OF_PAYMENT varchar(25), STATUS int(1));
 
`T_ID is generated randomly`

create table CART (C_ID int primary key, I_ID int, Name varchar(45), Qty int, Price int);

`may or may not remove Qty in the future`

create table DELIVERIES (T_ID int primary key, DESTINATION varchar(75), STATUS int(1));

`the destination is chosen randomly from a list of addresses`


## List of addresses:

Just because why not lmao


```py
ADDRESSES = ["8939 High Point St.","233 New Saddle St.","9197 Sunbeam Ave.","7800 E. Lake Forest Lane","224 Lower River St.","8603 Bedford Street","94 St Margarets Dr.","688 Buckingham Dr.","378 Beaver Ridge Drive","82 W. Main Circle","423 Birchpond Dr.","636 Westport St.","444 Armstrong St.","50 Essex St.","8876 Hudson Court","19 Spruce Drive","630 Hudson Street","56 East Windsor Street","7799 Queen Street","89 Meadowbrook Rd.","33 Smith Dr.","8271 Fordham Ave.","522 Prince Ave.","5 East Lilac Street","553 Trenton St."]
```


## Miscellaneous

Time to complete: approx 2 weeks

Software(s) used: VSCode, Notepad, GitHub, MySQL Command Client