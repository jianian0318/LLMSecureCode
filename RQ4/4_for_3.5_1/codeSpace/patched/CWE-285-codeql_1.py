from ctypes import CDLL, c_int, POINTER
from ctypes.util import find_library

libpam = CDLL(find_library("pam"))

pam_start = libpam.pam_start
pam_start.restype = c_int
pam_start.argtypes = [c_char_p, c_char_p, POINTER(PamConv), POINTER(PamHandle)]

pam_end = libpam.pam_end
pam_end.restype = c_int
pam_end.argtypes = [PamHandle, c_int]

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

class PamConv(Structure):
    _fields_ = [("conv", CFUNCTYPE(c_int, c_int, POINTER(PamMessage), POINTER(POINTER(PamResponse)), c_void_p))]

class PamMessage(Structure):
    _fields_ = [("msg_style", c_int), ("msg", c_char_p)]
    
class PamResponse(Structure):
    _fields_ = [("resp", c_char_p), ("resp_retcode", c_int)]

class PamHandle(Structure):
    _fields_ = [("handle", c_void_p)]

def my_conv(n_messages, messages, p_response, app_data):
    response = []
    
    for i in range(n_messages):
        if messages[i].msg_style == PAM_PROMPT_ECHO_OFF:
            password = password.encode('utf-8')
            buf = create_string_buffer(password)
            reply = PamResponse(buf, 0)
            response.append(reply)
    
    p_response.contents = (PamResponse * n_messages)(*response)
    
    return 0

def authenticate(username, password, service='login'):
    conv_func = CFUNCTYPE(c_int, c_int, POINTER(PamMessage), POINTER(POINTER(PamResponse)), c_void_p)(my_conv)
    pam_conv = PamConv(conv_func)
    
    handle = PamHandle()
    retval = pam_start(service, username, pam_conv.pointer, byref(handle))
    
    if retval != PAM_SUCCESS:
        pam_end(handle, retval)
        return False
    
    retval = pam_authenticate(handle, 0)
    pam_end(handle, retval)
    
    if retval == PAM_SUCCESS:
        return True
    else:
        return False