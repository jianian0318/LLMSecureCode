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
    return context
