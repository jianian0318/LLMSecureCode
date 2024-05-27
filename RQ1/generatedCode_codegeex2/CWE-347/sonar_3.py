import jwt

def verifyJWTToken(jwt_token):
    '''
    Verify the JWT Token and return it.
    '''
    try:
        decoded_token = jwt.decode(jwt_token, options={"verify_signature": False})
        return decoded_token
    except jwt.InvalidTokenError:
        return None
