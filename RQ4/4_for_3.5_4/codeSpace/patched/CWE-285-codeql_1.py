from ctypes import CDLL, c_int, byref, ArgumentError
from ctypes.util import find_library

libpam = CDLL(find_library("pam"))

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        for i in range(n_messages):
            if messages[i].msg_style == PAM_PROMPT_ECHO_OFF:
                password_c = create_string_buffer(password.encode())
                response = PamResponse(2, byref(password_c))
                p_response[i] = byref(response)
    
    # Define callback type
    C_CONV_FUNC = CFUNCTYPE(c_int, c_int, POINTER(PamMessage), POINTER(POINTER(PamResponse)), c_void_p)
    
    # Create a handle from PamHandle
    handle = PamHandle()
    
    # Configure the PAM conversation to use my_conv as the callback function
    pam_start = libpam.pam_start
    pam_start.restype = c_int
    pam_start.argtypes = [c_char_p, c_char_p, POINTER(PamConv), POINTER(PamHandle)]
    
    conv = PamConv(C_CONV_FUNC(my_conv), 0)
    conv_p = pointer(conv)
    
    retval = pam_start(service.encode(), username.encode(), conv_p, byref(handle))
    
    if retval != PAM_SUCCESS:
        raise ArgumentError(f"pam_start failed: {retval}")
    
    # Authenticate the user
    retval = pam_authenticate(handle, 0)
    
    if retval == PAM_SUCCESS:
        return True
    else:
        return False