import ssl

def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    # Create an SSL context
    context = ssl.create_default_context()
    
    # You can modify the context's settings here, if needed
    # For example, to skip hostname checking:
    # context.check_hostname = False
    
    # To skip certificate verification:
    # context.verify_mode = ssl.CERT_NONE
    
    return context

# Usage example
ssl_context = getSSLContext()