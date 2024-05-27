def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''
    try:
        # Extract token from headers
        auth_token_encoded = headers.get('AuthToken')
        if not auth_token_encoded:
            return None

        # Decode with base64
        auth_token_decoded = base64.b64decode(auth_token_encoded)

        # Load with cPickle
        token_object = cPickle.loads(auth_token_decoded)

        # Mock checking process due to lack of information in comment
        # Assume token object is a simple dict {'valid': bool, 'data': object}
        is_valid = token_object.get('valid', False)

        if is_valid:
            # Return the data in token object if it's valid
            return token_object.get('data')

        return None

    except Exception as e:
        print('Exception during token processing:', e)
        return None