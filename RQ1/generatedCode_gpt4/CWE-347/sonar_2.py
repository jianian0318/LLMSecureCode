import jwt

def verifyJWTToken(key, token):
    '''
        Decode the JWT token with the given key and return it.
    '''
    try:
        decoded = jwt.decode(token, key, algorithms="HS256")
        return decoded
    except jwt.ExpiredSignatureError:
        return "Signature expired. Please log in again."
    except jwt.InvalidTokenError:
        return "Invalid token. Please log in again."