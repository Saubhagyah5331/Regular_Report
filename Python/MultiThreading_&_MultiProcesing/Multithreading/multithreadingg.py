import threading
import time

def print_num():
    for i in range(5):
        time.sleep(1)
        print(i)
    
def print_letters():
    for letter in 'ABCD':
        time.sleep(1.5)
        print(letter)

#creating the threads   
thread1 = threading.Thread(target=print_num)
thread2 = threading.Thread(target=print_letters)

#starting the thread
thread1.start()
thread2.start()

#waith for both threads to finish
thread1.join()
thread2.join()

print("Finished Sucessfully")