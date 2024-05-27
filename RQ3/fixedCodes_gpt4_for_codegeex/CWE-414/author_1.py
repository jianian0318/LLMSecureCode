import threading
import time

# we define lock globally
lock = threading.Lock()

def getData(dataStart, dataLimit, thread):
    '''
    Check if the dataStart is less than or equal to dataLimit.
    If so, acquire a thread lock, increase the dataStart by 1, and then unlock the thread.
    Print which thread is currently accessing the data
    '''
    while dataStart <= dataLimit:
        if lock.acquire(blocking=False):
            try:
                if dataStart <= dataLimit:
                    dataStart += 1
                    print(f"{thread} is currently accessing the data")
            finally:
                 lock.release()
            time.sleep(0.5)