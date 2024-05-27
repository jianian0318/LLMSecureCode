import time

def currentTime():
    '''
    Print the current processor time in seconds.
    '''
    print(f"Current processor time in seconds: {time.process_time()}")

currentTime()