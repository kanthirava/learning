# print("1"*5)
# a=1
# while a < 5:
#     print(a*a)
#     a = a+1
# while a < 10:
#     b = 1
#     while b <= a:
#         print(b,end=" ")
#         b = b + 1
#     a = a+1
#     print()
# while a < 10:
#     b = 1
#     while b <= a:
#         print(a,end=" ")
#         b = b + 1
#     a = a+1
#     print()
def loops(a):
    while a >= 1:
        b=1
        while b >= a:
            print(b)
            b = b-1
    a = a-1
    print()
loops(4)