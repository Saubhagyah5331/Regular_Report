# Write a program that repeatedly asks the user to enter a positive number. If the user enters a negative number or zero, the program should 
# display an error message and ask again. The program should stop when the user enters a valid positive number and print the number.


Posnum = False

while Posnum != True:
    Usernum = int(input("Enter the Number: "))

    if Usernum > 0:
        Posnum = True
        print("You entered: ", Usernum)
    
    else:
        print("Invalid input. Try again.")
