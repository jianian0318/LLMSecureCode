import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''
    authToken = headers.get('AuthToken')
    
    if authToken:
        authToken = base64.b64decode(authToken)
        
        try:
            token = cPickle.loads(authToken)
            
            if token.get('isValid'):
                return token.get('data')
            
        except Exception as e:
            print(f'Error loading token: {str(e)}')
    
    return None