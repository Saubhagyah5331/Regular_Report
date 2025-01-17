# Write a program to check if a number is positive, negative, or zero.

num = int(input("Enter the number: "))

if num == 0:
    print("The enter number is zero")
elif num > 0:
    print("the number is positive: ", num)
else:
    print("The number is negative: ", num)