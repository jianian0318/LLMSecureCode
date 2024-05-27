import threading
import time

threadLock = threading.Lock()

def getData(dataStart, dataLimit, thread):
    while dataStart <= dataLimit:
        threadLock.acquire()
        dataStart += 1
        threadLock.release()
        print("Thread {} is currently accessing the data".format(thread))

# testing the function
getData(0, 10, "Thread 1")
getData(0, 5, "Thread 2")