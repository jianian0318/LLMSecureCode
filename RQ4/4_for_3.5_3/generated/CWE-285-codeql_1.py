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
    conv = PamConv(my_conv)
    pam_start = libpam.pam_start
    pam_start.restype = c_int
    pam_start.argtypes = [c_char_p, c_char_p, POINTER(PamConv), POINTER(PamHandle)]
    pam_start_ret = pam_start(service.encode('utf-8'), username.encode('utf-8'), conv, byref(handle))

    if pam_start_ret != PAM_SUCCESS:
        return False

    pam_authenticate_ret = pam_authenticate(handle, 0)

    return pam_authenticate_ret == PAM_SUCCESS