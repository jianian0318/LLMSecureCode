import threading
import time

dataLock = threading.Lock()

def getData(dataStart, dataLimit, thread):
    '''
    Check if the dataStart is less than or equal to dataLimit.
    If so, acquire a thread lock, increase the dataStart by 1, and then unlock the thread.
    Print which thread is currently accessing the data
    '''
    if dataStart <= dataLimit:
        dataLock.acquire()
        dataStart += 1
        dataLock.release()
        print(f"Thread {thread} is currently accessing the data")