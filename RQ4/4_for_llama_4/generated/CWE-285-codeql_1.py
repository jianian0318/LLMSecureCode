from ctypes import CDLL, POINTER, Structure, CFUNCTYPE, c_int, c_char_p, c_void_p
from ctypes.util import find_library

# Define the structure of the pam_conv structure
class PamConv(Structure):
    _fields_ = [
        ('conv', CFUNCTYPE(c_int, c_int, POINTER(c_void_p), POINTER(c_void_p), c_void_p)),
        ('appdata_ptr', c_void_p)
    ]

# Define the structure of the pam_handle_t structure
class PamHandle(Structure):
    _fields_ = [
        ('handle', c_void_p)
    ]

# Load the libpam shared library
libpam = CDLL(find_library("pam"))

# Get the pam_authenticate function from the library
pam_authenticate = libpam.pam_authenticate

# Define the return and argument types of pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        addr = calloc(n_messages, sizeof(PamResponse))
        p_response[0] = addr
        for i in range(n_messages):
            if messages[i].contents.msg_style == PAM_PROMPT_ECHO_OFF:
                cs = c_char_p(password)
                dst = calloc(sizeof(c_char_p), len(password) + 1)
                memmove(dst, cs, len(password) + 1)
                p_response.contents[i].resp = dst
                p_response.contents[i].resp_retcode = 0
        return 0

    handle = PamHandle()
    conv = PamConv(my_conv, 0)
    retval = pam_start(service, username, byref(conv), byref(handle))

    if retval != 0:
        # TODO: Handle this appropriately
        return False

    retval = pam_authenticate(handle, 0)
    return retval == 0