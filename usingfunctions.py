# # fibonacci numbers using functions
def fibmax(a=0, b=1, x=0):
    num= int(input("Enter range: "))
    while (x<=num):
        x = a+b
        a=b
        b=x
        print(x, end=" ")
fibmax()

# # reverse of the number
# def rev(x=0):
#     n = input("Enter a number: ")
#     rev = 0
#     while n>0:
#         d = n%10
#         rev = (rev*10) + d
#         n = n//10
#     print("Reverse of the number is: ",rev)
# rev()