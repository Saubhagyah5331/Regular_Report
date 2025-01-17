#  Write a program that attempts to divide two numbers provided by the user. If the user enters non-numeric input or tries to divide by zero, handle the exception with a try-except block.

try:
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    result = num1 / num2

except ZeroDivisionError:
    print("Zero cannot be divisible.")
except ValueError:
    print("Please Enter the Valid Number.")
finally:
    print(float(result))


