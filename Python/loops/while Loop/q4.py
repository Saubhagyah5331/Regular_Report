# Write a program that asks the user to enter a number. Use a while loop to count down from that number to 0, printing each number. When the countdown reaches 0, print "Liftoff!"

num = int(input("Enter the Number: "))

while num != -1:
    if num == 0:
        print("Liftoff")
        break
    print(num)
    num-=1
