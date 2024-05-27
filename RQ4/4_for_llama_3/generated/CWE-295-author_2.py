from OpenSSL import SSL

def getContext():
    # Create a new OpenSSL context
    context = SSL.Context(SSL.SSLv23_METHOD)

    # Set the context options
    context.set_options(SSL.OP_NO_SSLv2)
    context.set_options(SSL.OP_NO_SSLv3)

    # Set the context verify mode and depth
    context.set_verify(SSL.VERIFY_PEER, verify_cb)
    context.set_verify_depth(9)

    # Load the default OpenSSL CA certificates
    context.load_verify_locations(None, SSL.get_default_verify_paths())

    return context