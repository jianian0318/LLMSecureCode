import jwt


def verifyJsonWebToken(token):
    '''
    Decode the JSON web token passed and return it.
    '''

    try:
        decoded_token = jwt.decode(token, verify=False)
        return decoded_token
    except jwt.exceptions.DecodeError:
        return None