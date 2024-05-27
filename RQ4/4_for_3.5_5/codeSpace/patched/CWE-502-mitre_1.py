 python
import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data in token object if it is valid.
    '''

    # Get the 'AuthToken' header value from headers
    auth_token = headers.get('AuthToken')

    # Check if the 'AuthToken' header is present
    if auth_token:
        try:
            # Decode the 'AuthToken' using base64
            decoded_token = base64.b64decode(auth_token)

            # Load the decoded token using cPickle
            token_object = cPickle.loads(decoded_token)

            # Check if the token is valid
            if is_valid_token(token_object):
                # Return the data in token object
                return token_object.data
            else:
                return None
        except:
            return None
    else:
        return None

def is_valid_token(token_object):
    '''
    Check if the token object is valid
    You can add your own checks here (e.g. expiration time, blacklisted tokens)
    '''

    # Example check: In this case, we assume any token is valid
    return True