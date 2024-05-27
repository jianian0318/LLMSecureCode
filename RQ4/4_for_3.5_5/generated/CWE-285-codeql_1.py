from ctypes import *
from ctypes.util import find_library

# Load the libpam library
libpam = CDLL(find_library("pam"))

# Define the return type and argument types for the pam_authenticate function
pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        return c_int(0)  # Always return 0 to indicate success
    
    # Create a handle from PamHandle
    handle = PamHandle()
  
    # Configure the PAM conversation to use my_conv as a callback function
    conv = Conversation(CFUNCTYPE(c_int, c_int, POINTER(PamMessage), POINTER(POINTER(PamResponse)), c_void_p))
    convData = conv(my_conv)
    handle.conversation = convData
    
    # Authenticate the user
    result = pam_authenticate(handle, 0)
    
    # Return True if the authentication succeeded
    return result == PAM_SUCCESS

# Define the PamHandle and PamMessage structures
class PamHandle(Structure):
    _fields_ = [("handlePtr", c_void_p)]

class PamMessage(Structure):
    _fields_ = [("msgStyle", c_int),
                ("msg", c_char_p)]

# Define the PAM_SUCCESS constant
PAM_SUCCESS = 0