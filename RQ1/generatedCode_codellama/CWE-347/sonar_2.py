import jwt


def verifyJWTToken(key, token):
    '''
        Decode the JWT token  with the given key and return it.
    '''
    try:
        decoded_token = jwt.decode(token, key, algorithms=['HS256'])
        return decoded_token
    except jwt.exceptions.InvalidSignatureError:
        return None
