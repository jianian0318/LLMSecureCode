# The existing code is missing a section for validating the certificates. This fixed version includes verification, loading the system's cert file, and setting the verification flags to SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT. Here's how to do it

from OpenSSL import SSL

def verify_cb(conn, cert, errnum, depth, ok):
    # This obviously has to be updated
    print('Got certificate: %s' % cert.get_subject())
    return ok

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

    # New code begins here
    context.set_verify(SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verify_cb)
    try:
        context.load_verify_locations(None, "/etc/ssl/certs/")
    except:
        raise Exception('No cert file')
    return context


# The function `load_verify_locations` is used to set the location of the CA certificates that should be trusted. If it is set to None, it tries to load the default system certificates. The path "/etc/ssl/certs/" depending on the system, you will need to use the correct path.
#
# You also need to define a function `verify_cb`, which will be called for each certificate in the certificate chain, following the signature you see above.
#
# For better functionality, you may want to replace the print statement in verify_cb with a stronger validation check (complicated processing or custom logic) based on your specific case. Different applications may perform different types of validation.