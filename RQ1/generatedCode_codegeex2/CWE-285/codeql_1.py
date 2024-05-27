libpam                    = CDLL(find_library("pam"))

pam_authenticate          = libpam.pam_authenticate
pam_authenticate.restype  = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        for msg in messages:
            if msg.contents.msg_style == PAM_PROMPT_ECHO_OFF:
                p_response[0] = create_string_buffer(password.encode())
                return PAM_SUCCESS
        return PAM_CONV_ERR

    # 创建一个PamHandle句柄
    pamh = PamHandle()
    
    # 配置PAM对话，使用my_conv作为回调函数
    conv = PamConv(my_conv, 0)
    pamh.set_item(PAM_CONV, conv)
    
    # 使用pam_authenticate进行用户认证
    ret = pam_authenticate(pamh, 0)

    # 如果认证成功，返回True
    if ret == PAM_SUCCESS:
        return True
    else:
        return False
