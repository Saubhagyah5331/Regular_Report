# Example 2: Subclassing Thread

import threading

class Mythread(threading.Thread):
    def run(self):
        for _ in range(5):
            print("Hello world")
    

thread = Mythread()
thread.start()
thread.join()