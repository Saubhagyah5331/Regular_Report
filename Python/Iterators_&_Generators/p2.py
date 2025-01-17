# Write a generator function that yields the Fibonacci sequence up to a given number.
# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibo(end):
    a, b = 0, 1
    for _ in range(end):
        if a<=end:
            yield a
            a, b = b, a+b

for i in fibo(4):
    print(i)