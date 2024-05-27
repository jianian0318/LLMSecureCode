from ctypes import *
from ctypes.util import find_library

libpam = CDLL(find_library("pam"))

class PamHandle(Structure):
    pass

class PamMessage(Structure):
    pass

class PamResponse(Structure):
    pass

class PamConv(Structure):
    pass

PamHandle._fields_ = [
    ("handle", c_void_p),
]

PamMessage._fields_ = [
    ("msg_style", c_int),
    ("msg", c_char_p),
]

PamResponse._fields_ = [
    ("resp", c_char_p),
    ("resp_retcode", c_int),
]

PamConv._fields_ = [
    ("conv", CFUNCTYPE(c_int, c_int, POINTER(PamMessage), POINTER(POINTER(PamResponse)), c_void_p)),
    ("appdata_ptr", c_void_p),
]

pam_start = libpam.pam_start
pam_start.restype = c_int
pam_start.argtypes = [c_char_p, c_char_p, POINTER(PamConv), POINTER(PamHandle)]

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        addr = c_char_p(password.encode('utf-8'))
        p_response[0] = pointer(PamResponse(resp=addr))
        return 0

    handle = PamHandle()
    conv = PamConv(conv=CFUNCTYPE(c_int, c_int, POINTER(PamMessage), POINTER(POINTER(PamResponse)), c_void_p)(my_conv), appdata_ptr=c_void_p())
    pam_start(service.encode('utf-8'), username.encode('utf-8'), pointer(conv), pointer(handle))
    retval = pam_authenticate(handle, 0)
    return retval == 0
