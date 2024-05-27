import _pickle as cPickle
import base64


def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data in token object if it is valid.
    '''

    token = headers.get('AuthToken')
    
    if token:
        decoded_token = base64.b64decode(token)
        try:
            token_object = cPickle.loads(decoded_token)
            if is_valid_token(token_object):
                return token_object.data
        except cPickle.UnpicklingError:
            pass
    
    return None