#fibonacci numbers using functions
def fibmax(a=0, b=1, x=0):
    num= int(input("Enter range: "))
    while (x<=num):
        x = a+b
        a=b
        b=x
        print(x, end=" ")
fibmax()