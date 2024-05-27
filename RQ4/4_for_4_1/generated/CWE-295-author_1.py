import ssl

def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    ssl_context = ssl.create_default_context()
    return ssl_context