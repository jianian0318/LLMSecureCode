import ssl

def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    # Create a default SSL context
    context = ssl.create_default_context()
    
    return context