import jwt


def verifyJsonWebToken(token):
    '''
    Decode the JSON web token passed and return it.
    '''
    try:
        decoded_token = jwt.decode(token, "secret", algorithms=["HS256"])
        return decoded_token
    except jwt.exceptions.DecodeError:
        return "Invalid token"
