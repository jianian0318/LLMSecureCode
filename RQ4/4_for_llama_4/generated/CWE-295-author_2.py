from OpenSSL import SSL

def getContext():
    # Create a new OpenSSL context
    context = SSL.Context(SSL.TLSv1_2_METHOD)

    # Set the context options
    context.set_options(SSL.OP_NO_SSLv2)
    context.set_options(SSL.OP_NO_SSLv3)

    # Set the context mode
    context.set_mode(SSL.MODE_RELEASE_BUFFERS)

    # Return the context
    return context