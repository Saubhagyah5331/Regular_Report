# Nested Try-Except BlocksWrite a program that asks the user to input a number. The program should attempt to multiply the number by 2. If the number is negative, it should attempt to calculate the square root, which should be handled by a nested try-except block.
from math import sqrt

try:
    num = int(input("Enter the Number: "))
    multiply = num * 2
    print(multiply)
    
    try:
        if num < 0:
            sqt = sqrt(num)
    except:
        print("The Enter Number is negative.")
except:
    print("The numeber is negative.")
finally:
    print("The program get executed")
