import mysql.connector as mysql
mydb = mysql.connect(
    host= "localhost",
    user= "root",
    passwd= "",
    database= "kanthidb"
)
mycursor = mydb.cursor()

def insertStudentData(name,branch,year,phone,email):
    print(name,branch,year,phone,email)
    val = (name,branch,year,phone,email)
    mycursor.execute("INSERT INTO student_info (name,branch,year,phone,email) VALUES (%s,%s,%s,%s,%s)",val)
    mydb.commit()

i = input("Enter any of these Options 'i' or 'sh' or 'se' or 'de' or 'up' : ")
if(i=="i"):
    name = input("Enter Name : ")
    branch = input("Enter Branch : ")
    year = input("Enter year : ")
    phone = input("Enter phone : ")
    email = input("Enter Email : ")
    insertStudentData(name,branch,year,phone,email)
