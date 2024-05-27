from OpenSSL import SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    context.set_verify(SSL.VERIFY_PEER, verify_callback)
    return context

def verify_callback(conn, x509, errnum, depth, preverify_ok):
    '''
    Verify the certificate presented by the server.
    '''
    # Add your custom verification logic here
    # Return True if the certificate is valid, or False otherwise
    return True