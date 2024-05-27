import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data in token object if it is valid.
    '''
    authToken = headers.get('AuthToken')
    if not authToken:
        return None  # Return None if 'AuthToken' is not in headers

    # Decode it with base64
    decodedToken = base64.b64decode(authToken)
    
    try:
        # Load with cPickle to token object
        token = cPickle.loads(decodedToken)
    except cPickle.UnpicklingError:
        return None  # Return None if 'AuthToken' is not a valid cPickle object

    if checkToken(token):  # Implement this function separately
        # Return the data in token object if it is valid
        return token['data']
    else:
        return None

# define checkToken function here that checks if a token is valid or not
def checkToken(token):
    # Based on your token system, you will confirm whether the token is valid or not
    # this is a placeholder that always returns True
    return True