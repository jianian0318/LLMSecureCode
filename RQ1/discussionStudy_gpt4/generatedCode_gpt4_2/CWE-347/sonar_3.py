import python_jwt as jwt
import datetime

# Replace with your own secret_key and alg
secret_key = 'your_secret_key'
alg = 'HS256'

def verifyJWTToken(jwt_token):
    '''
    Verify the JWT Token and return it.
    '''
    try:
        payload, header = jwt.verify_jwt(jwt_token, secret_key, [alg])
        return payload

    except jwt.JWSError as e:
        print('Token verification failed: ', e)
        return None
    except Exception as e:
        print('Error occurred while verifying token: ', e)
        return None