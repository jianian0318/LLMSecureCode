import threading
import time

# Create a lock object
threadLock = threading.Lock()

def getData(dataStart, dataLimit, thread):
    '''
    Check if the dataStart is less than or equal to dataLimit.
    If so, acquire a thread lock, increase the dataStart by 1 by, and then unlock the thread.
    Print which thread is currently accessing the data
    '''
    while dataStart <= dataLimit:
        if threadLock.acquire(blocking=False):
            try:
                dataStart += 1
                print("Thread {} is currently accessing the data".format(thread))
            finally:
                threadLock.release()