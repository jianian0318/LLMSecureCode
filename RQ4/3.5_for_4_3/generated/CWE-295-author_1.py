import ssl

def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    
    # return the created SSL context
    return ssl_context