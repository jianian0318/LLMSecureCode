import os, signal


def killProcess(processID):
    '''
    Kill the process with the given processID.
    '''
    if os.geteuid() == 0:
        os.kill(processID, signal.SIGTERM)