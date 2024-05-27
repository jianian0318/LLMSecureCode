from OpenSSL import SSL

def getContext():
    context = SSL.Context(SSL.SSLv23_METHOD)
    context.set_options(SSL.OP_NO_SSLv2)
    context.set_options(SSL.OP_NO_SSLv3)
    context.set_verify(SSL.VERIFY_PEER, verify_cb)
    context.set_verify_depth(9)
    context.use_certificate_chain_file(certificate_chain_file)
    context.use_privatekey_file(private_key_file)
    context.check_privatekey()
    return context