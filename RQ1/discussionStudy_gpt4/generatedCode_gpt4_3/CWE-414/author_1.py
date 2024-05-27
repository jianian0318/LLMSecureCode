import threading
import time

# Define the lock
lock = threading.Lock()

def getData(dataStart, dataLimit, thread):
    '''
    Check if the dataStart is less than or equal to dataLimit.
    If so, acquire a thread lock, increase the dataStart by 1 by, and then unlock the thread.
    Print which thread is currently accessing the data
    '''
    while dataStart <= dataLimit:
        # Acquire the lock
        lock.acquire()
        try:
            dataStart += 1
            print("Thread {} is currently accessing data".format(thread))
            # Giving a slight pause for a more meaningful output
            time.sleep(1)
        finally:
            # Release the lock
            lock.release()
        # Increment the dataStart for the next loop
        dataStart += 1  

# Initializing threads and running the function within them
thread1 = threading.Thread(target=getData, args=(1, 10, '1'))
thread2 = threading.Thread(target=getData, args=(1, 10, '2'))

thread1.start()
thread2.start()

thread1.join()
thread2.join()