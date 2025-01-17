# Write a function called is_even(number) that takes an integer as input and returns True if the number is even and False otherwise. Test the function with the numbers 4 and 7 and print the results.

def is_even(num):
    
    if num % 2 == 0:
        return True
    return False

x = int(input("Please Enter the Number: "))

print(is_even(x))