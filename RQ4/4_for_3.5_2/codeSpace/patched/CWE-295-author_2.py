def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    context = SSL.Context(SSL.SSLv23_METHOD)
    return context