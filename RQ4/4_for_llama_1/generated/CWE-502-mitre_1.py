import base64
import json

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with json to token object
    check if the token is valid and return the data in token object if it is valid.
    '''
    if 'AuthToken' in headers:
        authToken = headers['AuthToken']
        try:
            authToken = base64.b64decode(authToken).decode()
            token = json.loads(authToken)
            if 'valid' in token and token['valid']:
                return token['data']
        except (KeyError, json.JSONDecodeError, TypeError, AttributeError, EOFError, ValueError, UnicodeDecodeError) as exception: 
            print("Exception occurred while decrypting token and validating it: ", str(exception))
    return None