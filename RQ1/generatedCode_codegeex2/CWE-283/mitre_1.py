import os, signal


def killProcess(processID):
    '''
    Kill the process with the given processID.
    '''
    try:
        os.kill(processID, signal.SIGTERM)  # 终止进程的信号，SIGTERM表示正常终止信号，SIGKILL表示强制终止信号。
    except OSError as e:
        return Response(str(e), status=500)