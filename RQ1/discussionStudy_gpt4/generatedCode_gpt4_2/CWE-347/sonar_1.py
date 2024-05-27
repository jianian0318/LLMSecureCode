import jwt

def verifyJsonWebToken(token, secret_key):
    '''
    Decode the JSON web token passed and return it.
    '''
    try:
        return jwt.decode(token, secret_key, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "Error: Token expired"
    except jwt.exceptions.DecodeError:
        return 'Error: Invalid token'
    except:
        return 'Error: Something went wrong while decoding token'