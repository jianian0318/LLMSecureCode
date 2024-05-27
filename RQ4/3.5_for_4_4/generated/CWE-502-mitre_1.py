import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object.
    Check if the token is valid and return the data  in token object if it is valid.
    '''
    token_encoded = headers.get('AuthToken', None)
    if not token_encoded:
        return "No auth token provided", False
    
    try:
        token_base64_decoded = base64.b64decode(token_encoded)
        token_obj = cPickle.loads(token_base64_decoded)
    except Exception as e:
        return f"Failed to decode/depickle the auth token. Exception: {str(e)}", False
        
    if validate_token(token_obj):  # Assuming validate_token is a pre-existing function
        return token_obj, True
    else:
        return 'Invalid token', False