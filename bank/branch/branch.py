import mysql.connector as mysql

mydb = mysql.connect(host="localhost",user="root",passwd="",database="bank",port=3306)
mycursor = mydb.cursor()

rep = "y"
def branch_creation():
    bank_name   = input("Enter Bank name: ")
    bank_branch = input("Enter branch name: ")
    bank_code   = input("Enter bank code: ")
    bank_ifsc   = input("Enter IFSC code: ")
    mycursor.execute("INSERT into branch (bank_name,branch,code,ifsc) VALUES (%s,%s,%s,%s)",(bank_name,bank_branch,bank_code,bank_ifsc))
    mydb.commit()
    print("Created successfully.")
    
    rep = input("'y' to Create another or 'n' to exit...")
    if (rep=="y"):
        branch_creation()
    else:
        print("Done!")

def bank_details():
    mycursor.execute("SELECT * from branch")
    result = mycursor.fetchall()
    for rows in result:
        print(rows)