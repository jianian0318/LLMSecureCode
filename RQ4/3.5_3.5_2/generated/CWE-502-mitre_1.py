def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''
    # Get the AuthToken from the headers
    auth_token = headers.get('AuthToken')

    # Decode the AuthToken using base64
    decoded_token = base64.b64decode(auth_token)

    # Load the decoded token object using cPickle
    token = cPickle.loads(decoded_token)

    # Check if the token is valid
    if token.is_valid():
        # Return the data in the token object
        return token.get_data()