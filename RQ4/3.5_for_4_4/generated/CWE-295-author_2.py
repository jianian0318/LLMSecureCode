from OpenSSL import SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    ctx = SSL.Context(SSL.SSLv23_METHOD)
    return ctx