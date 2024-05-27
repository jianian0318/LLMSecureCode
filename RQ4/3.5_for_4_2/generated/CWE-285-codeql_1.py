from ctypes import CDLL, c_int, POINTER, c_void_p
from ctypes.util import find_library

libpam = CDLL(find_library("pam"))

# Define restype and argtypes for pam_authenticate
pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [c_void_p, c_int]

PamHandle = c_void_p

# Structure for PAM message
class PamMessage(Structure):
    _fields_ = [
        ("msg_style", c_int),
        ("msg", c_char_p)
    ]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any
        prompt where the echo is off with the supplied password
        """
        # Ignore unused arguments
        _ = (n_messages, messages, p_response, app_data)
        
        # Return PAM_CONV_ECHO_OFF
        if messages.pointee.contents.msg_style == 1:
            return password
        else:
            return None

    # Create a handle from PamHandle
    handle = PamHandle()

    # Configure the PAM conversation
    libpam.pam_start(service, username, my_conv, None, byref(handle))

    # Authenticate the user
    ret = libpam.pam_authenticate(handle, 0)

    # Cleanup PAM handle
    libpam.pam_end(handle, ret)

    # Return true if the authentication succeeded, false otherwise
    return ret == 0