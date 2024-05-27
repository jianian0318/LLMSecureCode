import jwt

def verifyJsonWebToken(token, secret_key):
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jwt.InvalidSignatureError:
        print("Token signature is invalid.")
    except jwt.InvalidTokenError:
        print("Token is invalid.")
    except Exception as e:
        print(f"An error occurred while decoding the token: {str(e)}")
        return None