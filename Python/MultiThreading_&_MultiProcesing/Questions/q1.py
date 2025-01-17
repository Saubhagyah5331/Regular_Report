# Write a Python program using the threading module to print numbers from 1 to 10, one number every 2 seconds.
import threading
import time
def print_num():
    for i in range(1, 11):
        time.sleep(2)
        print(i)
    
#create Thread
Thread1 = threading.Thread(target=print_num)

    

#Start
Thread1.start()

#join

Thread1.join()

print("Scucess")