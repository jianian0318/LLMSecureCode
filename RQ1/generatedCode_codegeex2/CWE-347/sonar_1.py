import jwt


def verifyJsonWebToken(token):
    '''
    Decode the JSON web token passed and return it.
    '''
    try:
        decoded_token = jwt.decode(token, verify=False, algorithms=['HS256'])
        return decoded_token
    except jwt.exceptions.InvalidTokenError as e:
        print(f"Invalid token: {e}")