from OpenSSL import SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    # Create OpenSSL Context
    context = SSL.Context(SSL.TLSv1_2_METHOD) # Use secure TLSv1.2 method instead of insecure SSLv3_METHOD
    
    return context