import threading

lock = threading.Lock()

shared_res = 0

def incre():
    global shared_res
    with lock: #  reducing the task to perform the lock.acquire() and lock.release() the lock
        for _ in range(100):
            shared_res += 1
        #lock.release() is applied here if we dont use the 'with'

threads = [threading.Thread(target=incre) for _ in range(5)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"The Result is {shared_res}")