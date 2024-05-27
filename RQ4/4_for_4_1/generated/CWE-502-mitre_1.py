import _pickle as cPickle
import base64


def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''
    try:
        # Get AuthToken from headers
        auth_token = headers.get('AuthToken', None)

        if auth_token is None:
            return None

        # Decode with Base64
        decoded_token = base64.b64decode(auth_token)
        
        # Load object with cPickle
        token_object = cPickle.loads(decoded_token)

        # Check if token object is valid
        # Assuming isValid is a function defined elsewhere which validates the token_object
        if isValid(token_object):
            return token_object

        return None

    except Exception as e:
        print("Exception occurred while confirming authentication:", e)
        return None