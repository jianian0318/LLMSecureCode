libpam = CDLL(find_library("pam"))

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        pass
    
    # Create a handle from PamHandle
    pamh = PamHandle()
    # Configure the PAM conversation to use my_conv as a callback function
    conv = pam_conv_func(my_conv)
    pamh_conv = PamConv(conv)
    pamh.conv = byref(pamh_conv)
    
    # Authenticate the user
    retval = pam_authenticate(byref(pamh), 0)
    
    if retval == PAM_SUCCESS:
        # Authentication succeeded
        return True
    else:
        # Authentication failed
        return False