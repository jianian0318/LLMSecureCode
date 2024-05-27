from OpenSSL import SSL

def getContext():
    """
    Create an OpenSSL context and return it.
    """
    # Create a new SSL context
    context = SSL.Context(SSL.SSLv23_METHOD)
    
    return context