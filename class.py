import mysql.connector as mysql
mydb = mysql.connect(host= "localhost", user = "root", passwd = "", database = "arithematic_operations")
mycursor = mydb.cursor()
def savingData(a,b,task,res):
    print(a,b,operation,res)
    mycursor.execute("INSERT INTO operations (a,b,operation,result) VALUES (%s,%s,%s,%s)",(a,b,task,res))
    mydb.commit()

pro='true'
while (pro=='true'):
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))

    operation = input("Enter add or sub or mul or div : ")

    class calculator:
        # def __init__ (self):
        #     self.a= 6
        #     self.b= 3
        def addition(self, a, b):
            return(a+b)
        
        def substraction(self, a, b):
            return(a-b)

        def multiplication(self, a, b):
            return(a*b)

        def division(self, a, b):
            return(a/b)

    c = calculator()
    res=0

    if(operation == "add"):
        res=c.addition(a,b)
        print(res)
        savingData(a,b,operation,res)
    elif(operation == "sub"):
        res=c.substraction(a,b)
        print(res)
        savingData(a,b,operation,res)
    elif(operation == "mul"):
        res=c.multiplication(a,b)
        print(res)
        savingData(a,b,operation,res)
    elif(operation == "div"):
        res=c.division(a,b)
        print(res)
        savingData(a,b,operation,res)
    else:
        print("Select any of the option...")       

    pro = input('enter true to repeat or enter false to end: ')

