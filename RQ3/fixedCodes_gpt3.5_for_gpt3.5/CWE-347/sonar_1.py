import jwt

def verifyJsonWebToken(token):
    try:
        decoded_token = jwt.decode(token, verify=True)
        return decoded_token
    except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidSignatureError):
        return None