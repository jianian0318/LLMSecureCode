import jwt

def verifyJsonWebToken(token):
    '''
    Decode the JSON web token passed and return it.
    '''
    try:
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        return decoded_token
    except Exception as e:
        print(f"An error occurred while decoding the token: {str(e)}")
        return None