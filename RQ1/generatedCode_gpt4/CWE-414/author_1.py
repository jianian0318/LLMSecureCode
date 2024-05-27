import threading
import time

# Define a lock object
lock = threading.Lock() 

def getData(dataStart, dataLimit, thread):
    while dataStart <= dataLimit:
        lock.acquire() 
        try: 
            print("Thread-{} accessing data: {}".format(thread, dataStart)) 
            dataStart += 1 
            time.sleep(1) 
        finally: 
            lock.release()  # unlock the thread