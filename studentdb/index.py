import mysql.connector as mysql

mydb = mysql.connect(host="localhost",user="root",passwd="",database="college",port=3306)
mycursor = mydb.cursor()

####### Insertion process  #######
def insertStudentData(name,branch,year,phone,email):
    print(name,branch,year,phone,email)
    val = (name,branch,year,phone,email)
    mycursor.execute("INSERT INTO student_info (name,branch,year,phone,email) VALUES (%s,%s,%s,%s,%s)",val)
    # val = [('Teja1','CSE',4,9999999999),('Teja2','ECE',4,9999999999),('Teja3','EEE',4,9999999999)]
    # mycursor.executemany("INSERT INTO student_info (name,branch,year,phone) VALUES (%s,%s,%s,%s)",val)
    mydb.commit()

####### Get data from database ######
def getAllStudentData():
    mycursor.execute("SELECT * FROM student_info")
    result = mycursor.fetchall()
    for rows in result:
        print(rows)

####### Get search data from database ######
def searchStudentData(branch):
    mycursor.execute("SELECT * FROM student_info WHERE branch=%s",branch)
    result = mycursor.fetchall()
    for rows in result:
        print(rows)

####### Update data in database ######
def updateStudentData():
    id = input("Enter id : ")
    name = input("Enter Name : ")
    branch = input("Enter Branch : ")
    year = input("Enter year : ")
    phone = input("Enter phone : ")
    email = input("Enter Email : ")
    upInput = (id,name, branch, year, phone, email)
    mycursor.execute("UPDATE student_info SET name=%s, branch=%s, year=%s, phone=%s, email=%s WHERE id=%s",upInput)
    mydb.commit()

###### Delete row from database ######
def deleteStudentData(id):
    mycursor.execute("DELETE FROM student_info where id = %s",(idDel,))
    mydb.commit()


i = input("Enter any of these Options 'i' or 'sh' or 'se' or 'de' or 'up' : ")
if(i=="i"):
    name = input("Enter Name : ")
    branch = input("Enter Branch : ")
    year = input("Enter year : ")
    phone = input("Enter phone : ")
    email = input("Enter Email : ")
    insertStudentData(name,branch,year,phone,email)
    print("Inserted")
    getAllStudentData()
elif(i=="sh"):
    getAllStudentData()
elif(i=="se"):
    branch = input("Enter Branch : ")
    searchStudentData(branch)
elif(i=="up"):
    updateStudentData()
    print("Updated")
    getAllStudentData()
elif(i=="de"):
    idDel = input("Enter id : ")
    deleteStudentData(id)
    print("Deleted successfully")
    print("Existing data")
    getAllStudentData()

else:
    print("Select something dude!")