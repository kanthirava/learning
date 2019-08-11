# # # prime_range = int(input("Enter range: "))
# # # x = 1

# minimum = int(input(" Please Enter the Minimum Value: "))
# maximum = int(input(" Please Enter the Maximum Value: "))

# Number = minimum

# while(Number <= maximum):
#     count = 0
#     i = 2
    
#     while(i <= Number//2):
#         if(Number % i == 0):
#             count = count + 1
#             break
#         i = i + 1

#     if (count == 0 and Number != 1):
#         print(" %d" %Number, end = '  ')
#     Number = Number  + 1
    



############################################
# prime = []
# n = int(input("Enter range: "))
# for i in range(n):
#     x = 1
#     count = 0
#     while (x<=i):
#         if ((i%x)==0):
#             count+=1
#         x+=1
#     if (count == 2):
#         prime.append(i)
# print(prime)


prime = []
p_range = int(input("Enter range: "))
for x in range(1,p_range):
    for j in range(2,x):
        if x%j==0:
            break
    else:
        prime.append(x)

# print(len(prime)-1) # print(prime)

rows = len(prime)-1
a,temp,temp2 = 0,0,0
while temp2<rows:
    b = 4
    c = 0
    temp2 = temp+a
    while b>=a:             # this loop is for spacing
        print(" ",end=" ")
        b -= 1
    for i in range(temp,temp2+1):
        if i>rows:
            break
        print(prime[i],end=" ")
        print(" ",end=" ")
    print(" ")
    # print(a," ",temp," ",temp2)
    a += 1
    temp = temp+a
# print(prime)