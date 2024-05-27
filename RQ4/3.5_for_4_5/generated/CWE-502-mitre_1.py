import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''
    try:
        # Get AuthToken from headers
        token = headers.get('AuthToken')
        
        if not token:
            return None
        
        # Decode it with base64
        decoded_token = base64.b64decode(token)
        
        # Load with cPickle to token object
        token_obj = cPickle.loads(decoded_token)
        
        # Check if the token is valid
        if not isinstance(token_obj, dict) or 'isValid' not in token_obj or not token_obj['isValid']:
            return None
        
        # Return the data in token object if it is valid
        return token_obj['data']
    
    except Exception as e:
        print(str(e))
        return None