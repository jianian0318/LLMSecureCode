import os, signal

def killProcess(processID):
    '''
    Kill the process with the given processID.
    '''
    try:
        os.kill(processID, signal.SIGTERM)
    except OSError:
        print(f"No process with the id {processID} exists")