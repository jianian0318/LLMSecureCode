import ssl

def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    # Creating an SSL context with default settings
    context = ssl.create_default_context()
    
    # Returning the created context
    return context

# Example usage:
ssl_context = getSSLContext()
print(ssl_context)