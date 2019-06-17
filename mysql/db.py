import mysql.connector as mysql

mydb=mysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mypython"
)
print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)

# mycursor.execute("create database mypython")
# mycursor.execute("create table mytable (ids int not null auto_increment, name varchar(30) not null, branch varchar(10) not null, year tinyint not null, primary key(ids))")
count = 0
mycursor.execute("show tables")
