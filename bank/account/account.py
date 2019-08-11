import mysql.connector as mysql
# import branch.bank_details

mydb = mysql.connect(host="localhost",user="root",passwd="",database="bank",port=3306)
mycursor = mydb.cursor()

# def account_number_gen():
#     pass

re = "y"
def account_creation():
    name        = input("Enter Full name: ")
    address     = input("Enter address: ")
    id_proof    = input("Enter Aadhar no: ")
    dob         = input("Enter DOB in YYYY-MM-DD format: ")
    print("These are the list of banks")
    # bank_details()
    account_type= input("Enter savings or current: ")
    mycursor.execute("INSERT INTO account (name,address,id_proof,dob,account_type) VALUES (%s,%s,%s,%s,%s)",(name,address,id_proof,dob,account_type))
    mydb.commit()
    print("Created successfully.")

    re  = input("Enter 'y' for create another accnt or 'n' for exit: ")
    if (re == "y"):
        account_creation()
    else:
        print("Done!")

def account_search():
    search_account = input("Enter Name: ")
    mycursor.execute("SELECT * FROM account WHERE name= '%s'", (search_account,))
    search_result = mycursor.fetchall()
    for i in search_result:
        print(i)
        # if (i == search_account):
        #     print(i[])
        # else:
        #     print("No account found.")

# account_search()