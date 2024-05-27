from OpenSSL import SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    # Create an SSL Context object with a specific method
    context = SSL.Context(SSL.TLS_METHOD)
    
    # Add additional context setup here if necessary, like setting up certificates:
    # context.use_certificate_file('/path/to/certificate')
    # context.use_privatekey_file('/path/to/private/key')
    
    # Return the context
    return context

# Example usage:
ssl_context = getContext()