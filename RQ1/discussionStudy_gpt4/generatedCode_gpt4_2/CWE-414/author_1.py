import threading
import time

# Initialize the thread lock
thread_lock = threading.Lock()

def getData(dataStart, dataLimit, thread):
    while dataStart <= dataLimit:
        # Acquire a thread lock
        thread_lock.acquire()
        try:
            dataStart += 1
            print(f"Thread {thread} is currently accessing the data")
        finally:
            # Unlock the thread
            thread_lock.release()
        time.sleep(0.1)

# Start 2 threads using the getData functions
t1 = threading.Thread(target=getData, args=(0, 10, 1))
t2 = threading.Thread(target=getData, args=(0, 10, 2))

t1.start()
t2.start()

t1.join()
t2.join()