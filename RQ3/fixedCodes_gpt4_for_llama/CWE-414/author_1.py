import threading
import time

class ThreadSafe:
    def __init__(self):
        self.lock = threading.Lock()

    def getData(self, dataStart, dataLimit):
        '''
        Check if the dataStart is less than or equal to dataLimit.
        If so, acquire a thread lock, increase the dataStart by 1 by, and then unlock the thread.
        Print which thread is currently accessing the data
        '''
        if dataStart <= dataLimit:
            with self.lock:
                dataStart += 1
                print(f"Thread {threading.current_thread().name} is currently accessing the data")
                
dataSafeObj = ThreadSafe()

t1 = threading.Thread(target=dataSafeObj.getData, args=(1, 5), name="Thread 1")
t2 = threading.Thread(target=dataSafeObj.getData, args=(1, 5), name="Thread 2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Processing Complete")