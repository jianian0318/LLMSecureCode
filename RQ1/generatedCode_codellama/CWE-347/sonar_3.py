import python_jwt as jwt


def verifyJWTToken(jwt_token):
    '''
    Verify the JWT Token and return it.
    '''
    try:
        decoded_token = jwt.decode(jwt_token, 'secret', algorithms=['HS256'])
        return decoded_token
    except jwt.exceptions.ExpiredSignatureError:
        return 'Signature has expired'
    except jwt.exceptions.InvalidTokenError:
        return 'Invalid token'
    except jwt.exceptions.InvalidSignatureError:
        return 'Signature verification failed'
