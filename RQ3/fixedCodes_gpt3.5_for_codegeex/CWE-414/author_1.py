import threading
import time

dataStart = 0
dataLimit = 10
lock = threading.Lock()

def getData(thread):
    '''
    Check if the dataStart is less than or equal to dataLimit.
    If so, acquire the lock, increase the dataStart by 1, and then release the lock.
    Print which thread is currently accessing the data.
    '''
    global dataStart
    if dataStart <= dataLimit:
        lock.acquire()
        dataStart += 1
        lock.release()
        print(f"{thread} is currently accessing the data")

# Create thread objects
thread1 = threading.Thread(target=getData, args=("Thread 1",))
thread2 = threading.Thread(target=getData, args=("Thread 2",))

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()