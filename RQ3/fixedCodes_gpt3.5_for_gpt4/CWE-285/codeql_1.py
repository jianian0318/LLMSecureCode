from ctypes import CDLL, c_int, POINTER, Structure, CFUNCTYPE
from ctypes.util import find_library

libpam = CDLL(find_library("pam"))

pam_start = libpam.pam_start
pam_start.restype = c_int
pam_start.argtypes = [c_char_p, c_char_p, CFUNCTYPE(c_int, c_int, POINTER(c_char_p), 
                      POINTER(POINTER(c_char_p)), c_void_p), c_void_p, POINTER(PamHandle)]

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

class PamHandle(Structure):
    _fields_ = [
        ("conv", CFUNCTYPE(c_int, c_int, POINTER(POINTER(c_char_p)), POINTER(POINTER(c_char_p)), c_void_p))
    ]

def my_conv(n_messages, messages, p_response, app_data):
    """
    Simple conversation function that responds to any prompt where the echo is off with the supplied password
    """
    pass

def authenticate(username, password, service='login'):
    handle = PamHandle()

    pam_start_result = pam_start(service.encode(), username.encode(), CFUNCTYPE(c_int, c_int, POINTER(c_char_p), POINTER(POINTER(c_char_p)), 
                                                      c_void_p)(my_conv), None, handle)

    if pam_start_result != 0:
        return False

    return pam_authenticate(handle, 0) == 0