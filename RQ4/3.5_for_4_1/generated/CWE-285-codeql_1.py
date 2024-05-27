from ctypes import CDLL, c_int
from ctypes.util import find_library

# Load the PAM module
libpam = CDLL(find_library("pam"))

# Define the pam authenticate function
pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    class PamHandle(object): 
        def __init__(self):
            pass
    
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        pass
    # Create a handle from PamHandle
    handle = PamHandle()
    
    # Configure the PAM conversation to use my_conv as a callback function 
    # to allow PAM to send messages to and get input from a user. 
    conv = my_conv
    
    # Setup PAM Authentication
    pam_start(service, username, conv, byref(handle))
    
    # Authenticate the user
    retval = pam_authenticate(handle, 0)
    
    # Check if authentication was successful
    if retval != PAM_SUCCESS:
        return False
    else:
        return True