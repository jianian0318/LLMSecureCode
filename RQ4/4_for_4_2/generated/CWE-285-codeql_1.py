from ctypes import CDLL, POINTER, Structure, CFUNCTYPE, cast, pointer, c_char_p, c_void_p, c_int
from ctypes.util import find_library

libpam = CDLL(find_library("pam"))

pam_conv_func = CFUNCTYPE(c_int, c_int, POINTER(POINTER(c_char_p)), POINTER(POINTER(c_void_p)), c_void_p)
class PamHandle(Structure):
    _fields_ = []

class PamMessage(Structure):
    _fields_ = [("msg_style", c_int), ("msg", c_char_p)]

class PamResponse(Structure):
    _fields_ = [("resp", c_char_p), ("resp_retcode", c_int)]

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [POINTER(PamHandle), c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        responses = (POINTER(PamResponse) * n_messages)()
        for i in range(n_messages):
            if messages[i].contents.msg_style == 1:  # PAM_PROMPT_ECHO_OFF
                responses[i] = pointer(PamResponse(c_char_p(password.encode()), 0))
            else:
                responses[i] = pointer(PamResponse(c_char_p(marshal("Unexpected message: {}".format(messages[i].contents.msg)))
        p_response^ = cast(responses, POINTER(c_void_p))
        return 0
    
    handle = POINTER(PamHandle)()
    conv = pam_conv_func(my_conv)
    retval = libpam.pam_start(service.encode(), username.encode(), pointer(conv), byref(handle))
    if retval:
        return False  
    retval = pam_authenticate(handle, 0)
    libpam.pam_end(handle, 0)
    return retval == 0