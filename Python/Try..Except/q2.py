# Write a program that handles multiple exceptions. It should ask the user for a number and try to divide 100 by that number. If the user enters a non-numeric input or zero, display appropriate error messages.

try:
    num = int(input("Please Enter the Number: "))
    result = 100/num
    print(result)
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")