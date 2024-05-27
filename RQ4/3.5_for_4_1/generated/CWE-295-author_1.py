import ssl

def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    # Create a default SSL context
    ssl_context = ssl.create_default_context()
    
    # You can customize the context here if needed
    # For example:
    # ssl_context.load_cert_chain(certfile="path/to/certificate.pem", keyfile="path/to/key.pem")
    
    return ssl_context

# Example usage:
# ctx = getSSLContext()