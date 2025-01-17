import multiprocessing
import time

def print_num():
    for i in range(4):
        time.sleep(1)
        print(i)
    
def print_letter():
    for i in "ABC":
        time.sleep(1.5)
        print(i)
    

#Creating the Process
Process1 = multiprocessing.Process(target=print_num)
Process2 = multiprocessing.Process(target=print_letter)

#starting the Process
Process1.start()
Process2.start()

#wating for both to complete
Process1.join()
Process2.join()

print("Finished Sucessfully")