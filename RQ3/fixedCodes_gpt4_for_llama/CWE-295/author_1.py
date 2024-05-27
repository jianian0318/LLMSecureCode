import ssl

def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    context = ssl.create_default_context()
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED
    return context