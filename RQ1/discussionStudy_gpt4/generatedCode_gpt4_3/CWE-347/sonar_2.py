import jwt


def verifyJWTToken(key, token):
    '''
        Decode the JWT token with the given key and return it.
    '''
    try:
        decoded_jwt_token = jwt.decode(token, key, algorithms=['HS256'])
        return decoded_jwt_token
    except jwt.ExpiredSignatureError:
        return "Signature has expired."
    except jwt.InvalidTokenError:
        return "Invalid token."