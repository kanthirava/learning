#fibonacci numbers
x=0
a=0
b=1
num=  int(input("Enter range: "))
while (x<=num):
    x=a+b
    a=b
    b=x
    print(x, end=" ")