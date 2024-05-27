from ctypes import CDLL, find_library, c_int
from ctypes import Structure, pointer

libpam = CDLL(find_library("pam"))


class PamHandle(Structure):
    pass


PamHandlePtr = pointer(PamHandle)


pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandlePtr, c_int]


def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        pass

    handle = PamHandle()
    handle_ptr = pointer(handle)

    # Configure the PAM conversation to use my_conv as a callback function
    libpam.pam_set_item(handle_ptr, c_int(8), my_conv)

    # Authenticate the user
    ret = pam_authenticate(handle_ptr, 0)

    # Return True if the authentication succeeded
    if ret == 0:
        return True
    else:
        return False