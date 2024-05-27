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

# Load the libpam library
libpam = CDLL(find_library("pam"))

# Define the pam_start function
pam_start = libpam.pam_start
pam_start.restype = c_int
pam_start.argtypes = [c_char_p, c_char_p, POINTER(PamConv), POINTER(PamHandle)]

# Define the pam_authenticate function
pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        addr = PamResponse * n_messages
        p_response[0] = addr()
        for i in range(n_messages):
            if messages[i].contents.msg_style == 1:
                pw_copy = c_char_p(password.encode('utf-8'))
                p_response.contents[i].resp = cast(pw_copy, c_void_p)
                p_response.contents[i].resp_retcode = 0
        return 0

    handle = PamHandle()
    conv = PamConv(my_conv, 0)
    pam_start(service.encode('utf-8'), username.encode('utf-8'), byref(conv), byref(handle))
    retval = pam_authenticate(handle, 0)
    return retval == 0