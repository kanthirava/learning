# transaction_id
# sender_id
# receiver_id
# amount
# transaction_date
# transaction_time
# transaction_type

import mysql.connector as mysql
import time

mydb = mysql.connect(host="localhost",user="root",passwd="",database="bank",port=3306)
mycursor = mydb.cursor()

def create_transaction():
    sender      = input("Enter sender Name: ")
    receiver    = input("Enter receiver Name: ")
    mode        = input("Enter mode of transfer (IMPS or RTGS or NEFT): ")
    amount      = int(input("Enter amount : "))
    
    mycursor.execute("SELECT `balance` FROM `account` WHERE `name` = %s",(sender,))
    res = mycursor.fetchone()
    if (res['balance']<amount):
        print("Insufficient Funds!")
    else:
        current_date = time.strftime('%Y-%m-%d %H:%M:%S')
        mycursor.execute("INSERT into `transactions` (id,date,sender,receiver,mode,amount) VALUES (NULL,%s,%s,%s,%s,%s)", (current_date,sender,receiver,mode,amount))
        mydb.commit()
        mycursor.execute("SELECT `name` FROM account WHERE `name` = %s",(receiver,))
        res2 = mycursor.fetchone()
        sbalance = res['balance'] - amount
        rbalance = res2['balance'] + amount
        mycursor.execute("UPDATE `account` SET `balance` = %s, WHERE `name` = %s",(sbalance,sender))
        mydb.commit()
        mycursor.execute("UPDATE `account` SET `balance` = %s, WHERE `name` = %s",(rbalance,receiver))
        mydb.commit()

        # mycursor.execute("UPDATE into `accounts` (balance) VAALUES (%s)", (balance,))