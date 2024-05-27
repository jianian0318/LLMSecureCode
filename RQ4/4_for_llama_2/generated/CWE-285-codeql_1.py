from ctypes import CDLL, POINTER, Structure, CFUNCTYPE, c_int, c_char_p, c_void_p
from ctypes.util import find_library

# Define the structure of the pam_conv structure
class PamConv(Structure):
    _fields_ = [
        ('conv', CFUNCTYPE(c_int, c_int, POINTER(c_void_p), POINTER(c_void_p), c_void_p)),
        ('appdata_ptr', c_void_p),
    ]

# Define the structure of the pam_handle_t structure
class PamHandle(Structure):
    _fields_ = [
        ('handle', c_void_p),
    ]

# Define the structure of the pam_message structure
class PamMessage(Structure):
    _fields_ = [
        ('msg_style', c_int),
        ('msg', c_char_p),
    ]

# Define the structure of the pam_response structure
class PamResponse(Structure):
    _fields_ = [
        ('resp', c_char_p),
        ('resp_retcode', c_int),
    ]

# Load the PAM library
libpam = CDLL(find_library("pam"))

# Get the pam_start function from the PAM library
pam_start = libpam.pam_start

# Define the arguments and return type of pam_start
pam_start.argtypes = [c_char_p, c_char_p, POINTER(PamConv), POINTER(PamHandle)]
pam_start.restype = c_int

# Get the pam_authenticate function from the PAM library
pam_authenticate = libpam.pam_authenticate

# Define the arguments and return type of pam_authenticate
pam_authenticate.argtypes = [PamHandle, c_int]
pam_authenticate.restype = c_int

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        addr = PamResponse(str.encode(password), 0)
        p_response[0] = addr
        return 0

    handle = PamHandle()
    conv = PamConv(CFUNCTYPE(c_int, c_int, POINTER(c_void_p), POINTER(c_void_p), c_void_p)(my_conv), 0)
    pam_start(service, username, byref(conv), byref(handle))
    retval = pam_authenticate(handle, 0)
    return retval == 0