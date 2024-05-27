def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    return ssl.create_default_context()