from OpenSSL import SSL

def getContext():
    # Create an OpenSSL context and return it.
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    return context