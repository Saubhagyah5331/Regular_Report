# Write a program that takes a list of integers [12, 7, 19, 24, 5, 16] and uses a for loop to identify and print only the prime numbers from the list.

lisnum = [12, 7, 19, 24, 5, 16]

primenum = []

for num in lisnum:
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primenum.append(num)

print("Prime Numbers: ",primenum)
        
