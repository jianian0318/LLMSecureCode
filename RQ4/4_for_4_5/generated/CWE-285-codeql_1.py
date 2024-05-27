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

    # Create handle. Note that PamHandle is undefined
    pam_handle = PamHandle()

    # Configure PAM conversation
    conversation = PamConversation(my_conv, 0)
    pam_start = libpam.pam_start
    pam_start(service, username, byref(conversation), byref(pam_handle))

    # Authenticate user
    result = pam_authenticate(pam_handle, 0)

    return True if result == 0 else False