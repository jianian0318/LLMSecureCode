import jwt

def verifyJsonWebToken(token, secret_key):
    '''
    Decode the JSON web token passed and return it.
    '''
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'], options={"verify_signature": True})
        return decoded_token
    except Exception as e:
        print(f"An error occurred while decoding the token: {str(e)}")
        return None


