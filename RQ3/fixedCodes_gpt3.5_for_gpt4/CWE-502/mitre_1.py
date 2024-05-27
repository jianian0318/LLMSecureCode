import pickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with pickle to token object
    check if the token is valid and return the data in token object if it is valid.
    '''
    token = headers.get('AuthToken')
    if token:
        try:
            # decode base64 encoding
            token = base64.b64decode(token)
            # load with pickle
            tokenObj = pickle.loads(token)
        except (TypeError, pickle.UnpicklingError, base64.binascii.Error) as e:
            return None

        # check the token validity
        # you could implement your own token validation logic here
        if 'expiry' in tokenObj and 'username' in tokenObj:
            return tokenObj   # return the data in token object
        else:
            return None

    return None