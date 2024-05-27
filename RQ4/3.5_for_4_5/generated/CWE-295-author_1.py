import ssl


def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    # Create an SSL context
    ssl_context = ssl.create_default_context()
    
    # Return the SSL context
    return ssl_context