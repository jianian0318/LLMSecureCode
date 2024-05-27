from OpenSSL import SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    context.set_options(SSL.OP_NO_SSLv2)
    context.set_options(SSL.OP_NO_SSLv3)
    context.set_options(SSL.OP_NO_TLSv1)
    context.set_options(SSL.OP_NO_TLSv1_1)
    context.set_cipher_list('HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!3DES')
    context.set_verify(SSL.VERIFY_PEER, verify_callback)
    context.load_verify_locations(cafile='ca.crt')
    return context

def verify_callback(conn, cert, errnum, depth, ok):
    '''
    Verify the SSL certificate.
    '''
    if not ok:
        raise SSL.Error

    return ok