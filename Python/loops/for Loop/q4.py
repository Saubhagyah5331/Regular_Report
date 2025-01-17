# Write a program that uses nested for loops to print a multiplication table for numbers 1 through 5. Format the output as shown below.

for x in range(1,6):
    for y in range(1,6):
        print(x*y, end=" ")
    print()