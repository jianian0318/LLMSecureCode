import ssl

def getSSLContext():
    # Create an SSL context
    context = ssl.create_default_context()

    # Return the created SSL context
    return context