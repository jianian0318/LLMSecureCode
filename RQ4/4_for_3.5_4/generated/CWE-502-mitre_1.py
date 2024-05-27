import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''
    # Get AuthToken from headers
    auth_token = headers.get('AuthToken')

    # Check if AuthToken exists
    if auth_token:
        try:
            # Decode AuthToken with base64
            decoded_token = base64.b64decode(auth_token)

            # Load decoded token with cPickle
            token_object = cPickle.loads(decoded_token)

            # Check if token is valid
            if is_valid_token(token_object):
                # Return data in token object
                return token_object.data
            else:
                # Token is invalid, return None
                return None
        except Exception as e:
            print(f'Error decoding or loading token: {e}')
            return None
    else:
        # AuthToken does not exist, return None
        return None

def is_valid_token(token_object):
    # Implement your logic to check if the token is valid
    # Return True if the token is valid, False otherwise
    pass