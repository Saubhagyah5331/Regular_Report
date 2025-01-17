# Write a function called factorial(n) that takes a positive integer n as input and returns its factorial.

def factorial(n):
    K=1
    for i in range(1, n+1):
        K=K*i
    return K
    # if n==0 or n==1:
    #     return 1
    # return n*factorial(n-1)

posnum = False
while posnum != True:
    num = int(input("Enter the Number: "))

    if num > 0:
        posnum = True
        print(factorial(num))

    else:
        posnum = False
        print("Please try again!!")

