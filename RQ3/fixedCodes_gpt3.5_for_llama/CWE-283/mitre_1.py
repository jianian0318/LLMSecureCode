import os, signal


def killProcess(processID):
    '''
    Kill the process with the given processID.
    '''
    try:
        os.kill(processID, signal.SIGTERM)
    except ProcessLookupError:
        print("No such process exists.")
    except PermissionError:
        print("Permission denied to kill the process.")
    except Exception as e:
        print("Error killing the process:", e)