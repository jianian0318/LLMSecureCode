from ctypes import CDLL, c_int
from ctypes.util import find_library

libpam = CDLL(find_library("pam"))

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        pass
    
    handle = PamHandle()
    handle.user = username
    handle.conv = my_conv
    handle.service = service
    handle.password = password

    result = pam_authenticate(handle, 0)

    if result == 0:
        return True
    else:
        return False

username = input("Enter username: ")
password = input("Enter password: ")
service = 'login'

authenticated = authenticate(username, password, service)
print(authenticated)