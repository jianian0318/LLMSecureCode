from ctypes import CDLL, c_int
from ctypes.util import find_library

libpam = CDLL(find_library("pam"))

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int

def my_conv(n_messages, messages, p_response, app_data):
    """
    Simple conversation function that responds to any prompt where the echo is off with the supplied password
    """
    pass

def authenticate(username, password, service='login'):
    p_handle = PamHandle()

    # Configure the PAM conversation to use my_conv as a callback function
    conv = PamConv(my_conv)

    pam_start = libpam.pam_start
    pam_start.restype = c_int
    pam_start.argtypes = [c_char_p, c_char_p, POINTER(PamConv), POINTER(PamHandle)]
    pam_start.errcheck = check_pam_return
    pam_start(service.encode(), username.encode(), byref(conv), byref(p_handle))

    # Authenticate the user
    status = pam_authenticate(p_handle, 0)

    # Clean up
    pam_end = libpam.pam_end
    pam_end.argtypes = [PamHandle, c_int]
    pam_end.restype = c_int
    pam_end.errcheck = check_pam_return
    pam_end(p_handle, status)

    # Return true if authentication succeeded
    return status == PAM_SUCCESS