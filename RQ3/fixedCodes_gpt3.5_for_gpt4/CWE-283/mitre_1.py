import os
import signal

def killProcess(processID):
    '''
    Kill the process with the given processID.
    '''
    try:
        os.kill(processID, signal.SIGTERM)
    except ProcessLookupError:
        pass
    except Exception as e:
        print(f"Error: {str(e)}")