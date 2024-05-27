libpam                    = CDLL(find_library("pam"))

pam_authenticate          = libpam.pam_authenticate
pam_authenticate.restype  = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        responses = (c_int * n_messages)()
        for i in range(n_messages):
            if messages[i].msg_style == PAM_PROMPT_ECHO_OFF:
                responses[i].resp = copy_string(password)
                responses[i].resp_retcode = PAM_SUCCESS
            else:
                responses[i].resp = NULL
                responses[i].resp_retcode = PAM_CONV_ERR
        p_response[0] = cast(responses, POINTER(c_int))
        return PAM_SUCCESS

    conv = PamConv(my_conv, 0)
    pam_handle = PamHandle()
    retval = libpam.pam_start(service, username, byref(conv), byref(pam_handle))

    if retval != PAM_SUCCESS:
        return False

    retval = pam_authenticate(pam_handle, 0)
    libpam.pam_end(pam_handle, retval)

    if retval != PAM_SUCCESS:
        return False

    return True