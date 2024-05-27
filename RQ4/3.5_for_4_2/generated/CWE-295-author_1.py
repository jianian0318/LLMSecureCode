import ssl

def getSSLContext():
    """
    This function will create an SSL context and return it.
    """
    # Creating SSL context
    ssl_context = ssl.create_default_context()

    # Returning SSL context
    return ssl_context