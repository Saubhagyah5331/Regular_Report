# Write a program that asks the user to guess a number (e.g., 7). Use a while loop to keep asking until the user guesses the correct number. Display a congratulatory message when they guess correctly.
gussnum = 6

usernum = False

while usernum != True:
    x = int(input("Enter the Number to guess: "))

    if x == gussnum:
        usernum = True
        print("Congratulations! You guessed it! ", x)
    
    else:
        print("Wrong! Try again.  ")