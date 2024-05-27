import ssl


def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH, cafile=None, capath=None, cadata=None, options=None, check_hostname=False)
    return context