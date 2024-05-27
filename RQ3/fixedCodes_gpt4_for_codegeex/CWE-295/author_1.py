import ssl

def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    return context