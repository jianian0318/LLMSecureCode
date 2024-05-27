import threading
import time


def getData(dataStart, dataLimit, thread):
    '''
    Check if the dataStart is less than or equal to dataLimit.
    If so, acquire a thread lock, increase the dataStart by 1 by, and then unlock the thread.
    Print which thread is currently accessing the data
    '''
    if dataStart <= dataLimit:
        thread.lock.acquire()
        dataStart += 1
        thread.lock.release()
        print(f"Thread {thread} is currently accessing the data")