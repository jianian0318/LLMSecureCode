import ssl


def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    context = ssl.create_default_context()  #  Create a new SSL context with default settings and protocol
    return context