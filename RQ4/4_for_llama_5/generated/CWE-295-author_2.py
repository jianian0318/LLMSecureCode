from OpenSSL import SSL

def getContext():
    # Create an OpenSSL context
    context = SSL.Context(SSL.TLSv1_2_METHOD)

    # Set the cipher list
    context.set_cipher_list('HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK')

    # Set the context options
    context.set_options(SSL.OP_NO_SSLv2 | SSL.OP_NO_SSLv3 | SSL.OP_NO_TLSv1 | SSL.OP_NO_TLSv1_1)

    # Set the context mode
    context.set_mode(SSL.MODE_RELEASE_BUFFERS)

    # Return the SSL context
    return context