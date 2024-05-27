from OpenSSL import SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    #Creating a new OpenSSL Context
    context = SSL.Context(SSL.SSLv23_METHOD)
    
    #Returning the newly created OpenSSL Context
    return context