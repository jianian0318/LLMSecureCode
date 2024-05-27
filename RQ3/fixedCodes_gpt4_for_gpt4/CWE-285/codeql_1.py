libpam = CDLL(find_library("pam"))

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        result = POINTER(pam_response)()
        response = pam_response()
        result.contents = response
        response.resp = copy_string(password)
        return 0

    # Creating a handle for PamHandle and setting conv attribute to my_conv callback function
    conv = PamConv(my_conv, password)
    handle_addr = pointer(PamHandle())
    error = libpam.pam_start(service, username, pointer(conv), pointer(handle_addr))

    if error != 0:
        return False

    handle = handle_addr.contents

    # Attempt to authenticate
    error = pam_authenticate(handle, 0)

    libpam.pam_end(handle, error)

    # Return True if the authentication succeeded
    return error == 0