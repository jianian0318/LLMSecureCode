from ctypes import CDLL, POINTER, Structure, CFUNCTYPE, cast, pointer, c_void_p, c_int, find_library

libpam = CDLL(find_library("pam"))

class PamMessage(Structure):
    _fields_ = [("msg_style", c_int), ("msg", c_char_p)]

class PamResponse(Structure):
    _fields_ = [("resp", c_char_p), ("resp_retcode", c_int)]

CONV_FUNC = CFUNCTYPE(c_int, c_int, POINTER(POINTER(PamMessage)), POINTER(POINTER(PamResponse)), c_void_p)

class PamConv(Structure):
    _fields_ = [("conv", CONV_FUNC), ("appdata_ptr", c_void_p)]

PamHandle = POINTER(c_void_p)

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        responses = (PamResponse * n_messages)()
        for i in range(n_messages):
            if messages[i].contents.msg_style == 1:
                responses[i].resp = create_string_buffer(password)
        p_response[0] = cast(responses, POINTER(PamResponse))
        return 0

    conv = PamConv(CONV_FUNC(my_conv), 0)
    pamh = PamHandle()
    retval = libpam.pam_start(service, username, pointer(conv), pointer(pamh))

    if retval != 0:
        return False

    retval = pam_authenticate(pamh, 0)

    if retval != 0:
        return False

    return True