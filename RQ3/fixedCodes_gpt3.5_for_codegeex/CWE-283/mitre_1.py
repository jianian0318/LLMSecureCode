import os, signal
from flask import Response

def killProcess(processID):
    '''
    Kill the process with the given processID.
    '''
    try:
        os.kill(processID, signal.SIGTERM)  # Terminate process signal, SIGTERM indicates normal termination, SIGKILL indicates forced termination signal.
    except OSError as e:
        return Response(str(e), status=500)