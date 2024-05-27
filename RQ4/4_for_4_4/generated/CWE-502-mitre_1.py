import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''
    if "AuthToken" in headers:
        # Get the AuthToken
        token_b64 = headers['AuthToken']
        
        # Decode base64 token into bytes
        token_bytes = base64.b64decode(token_b64)

        # Load token object from bytes
        token = cPickle.loads(token_bytes)
        
        # Assuming the token is a dictionary with a 'valid' field
        if 'valid' in token and token['valid']:
            # If the token is valid, return the data in the token object
            return token
        else:
            return "Invalid Token"
    else:
        return "AuthToken Header not found"