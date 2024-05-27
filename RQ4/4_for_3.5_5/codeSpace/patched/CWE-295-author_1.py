def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    context = ssl.create_default_context()
    return context