def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''

    # Get the AuthToken from headers
    auth_token = headers.get("AuthToken")

    # Decode the AuthToken with base64
    decoded_token = base64.b64decode(auth_token)

    # Load the decoded token with cPickle
    token_object = cPickle.loads(decoded_token)

    # Check if the token is valid
    if token_object.is_valid():
        # Return the data in token object if the token is valid
        return token_object.data
    else:
        # Return None if the token is invalid
        return None