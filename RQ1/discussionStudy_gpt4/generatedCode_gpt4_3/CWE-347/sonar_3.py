import python_jwt as jwt
import datetime

def verifyJWTToken(jwt_token, key):  # Updated function with necessary parameters
    '''
    Verify the JWT Token and return it.
    '''
    try:
        payload, header = jwt.verify_jwt(jwt_token, key, ['HS256'])
        return payload
    except Exception as e:   # catch exception if JWT token is incorrect
        print(f"Unable to verify JWT token: {str(e)}")