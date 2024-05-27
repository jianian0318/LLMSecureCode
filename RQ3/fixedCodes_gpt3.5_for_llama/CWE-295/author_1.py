import ssl


def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    context = ssl.create_default_context()
    context.check_hostname = False
    # Disabling certificate verification in production code is generally not recommended.
    # Instead, it is better to use a valid certificate and properly configure SSL/TLS.
    context.verify_mode = ssl.CERT_REQUIRED
    return context