import _pickle as cPickle
import base64


def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data in token object if it is valid.
    '''
    try:
        # Get AuthToken from headers
        token_string = headers.get('AuthToken')
        
        # Decode AuthToken with base64
        decoded_token = base64.b64decode(token_string.encode('utf-8'))
        
        # Load decoded token with cPickle to token object
        token_object = cPickle.loads(decoded_token)
        
        # Return data in token object if it is valid
        if is_valid_token(token_object):
            return token_object.data
        else:
            return None
    except (TypeError, base64.binascii.Error, cPickle.UnpicklingError):
        return None


def is_valid_token(token):
    # Implement your logic to check if the token is valid
    # Return True if the token is valid, False otherwise
    return True