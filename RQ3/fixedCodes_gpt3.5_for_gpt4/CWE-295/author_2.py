import OpenSSL.SSL as SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    # create new context
    context = SSL.Context(SSL.TLSv1_2_METHOD)

    # Set verification mode to verify the certificate
    context.set_verify(SSL.VERIFY_PEER, verify_callback)

    # return the context
    return context

def verify_callback(conn, cert, errnum, depth, ok):
    return ok