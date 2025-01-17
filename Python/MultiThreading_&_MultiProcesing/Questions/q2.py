# Write a Python program using the multiprocessing module to calculate the sum of numbers from 1 to 1000000 in parallel by splitting the range into two parts. Each part should be handled by a different process.

import multiprocessing

def sum_muli(start, end):
    return sum(range(start,end))


range1 = (1, 500000)
range2 = (500001, 1000001)
    
#create process
Process1 = multiprocessing.Process(target=sum_muli, args = range1)
Process2 = multiprocessing.Process(target=sum_muli, args = range2)

#start
Process1.start()
Process2.start()

#join
Process1.join()
Process2.join()
