import threading
import time

def getData(dataStart, dataLimit, thread):
    '''
    Check if the dataStart is less than or equal to dataLimit.
    If so, acquire a thread lock, increase the dataStart by 1, and then unlock the thread.
    Print which thread is currently accessing the data
    '''
    if dataStart <= dataLimit:
        lock = threading.Lock()
        lock.acquire()
        dataStart += 1
        lock.release()
        print(f"{thread} is currently accessing the data")
