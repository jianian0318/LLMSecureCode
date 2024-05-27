import os
import signal
import getpass
import psutil


def killProcess(processID):
    '''
    Kill the process with the given processID.
    '''
    try:
        process = psutil.Process(processID)
        # check if process user id is same as the current user id
        if process.uids().real == os.getuid():
            os.kill(processID, signal.SIGTERM)
        else:
            print("Ownership of the process cannot be verified")
    except psutil.NoSuchProcess:
        print("No process found with id {}".format(processID))