import ssl
from OpenSSL import SSL

def verify_cb(conn, cert, errnum, depth, ok):
    certsubject = crypto.X509Name(cert.get_subject())
    commonname = certsubject.commonName
    return ok

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    context.set_verify(SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verify_cb)
    try:
        context.load_verify_locations(None, "/etc/ssl/certs/") # Assuming trusted certificates are in this location
    except Exception as e:
        print("Certificate verification failed.")
    return context