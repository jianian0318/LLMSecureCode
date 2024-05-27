import jwt


def verifyJsonWebToken(token):
    try:
        decoded_token = jwt.decode(token, algorithms=['HS256'])
        return decoded_token
    except jwt.exceptions.InvalidTokenError as e:
        print(f"Invalid token: {e}")