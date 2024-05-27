from OpenSSL import SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    # create new context
    context = SSL.Context(SSL.TLSv1_2_METHOD)

    # return the context
    return context