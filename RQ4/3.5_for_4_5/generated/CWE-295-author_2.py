from OpenSSL import SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    context = SSL.Context(SSL.SSLv23_METHOD) # SSLv23_METHOD to use highest TLS/SSL version that both client and server support
    return context