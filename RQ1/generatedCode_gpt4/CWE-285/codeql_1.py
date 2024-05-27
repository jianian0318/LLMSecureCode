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

    # Creating a handle from PamHandle
    handle = PamHandle()

    # Configuring the PAM conversation to use my_conv as a callback function
    handle.conv = my_conv

    # Authenticating the user and returning true if the authentication is succeeded
    return pam_authenticate(handle, 0) == 0