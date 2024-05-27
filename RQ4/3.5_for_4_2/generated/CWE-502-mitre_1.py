import _pickle as cPickle
import base64

def confirmAuth(headers):
    # Check that headers dictionary contains 'AuthToken'
    if 'AuthToken' not in headers:
        return None

    #Get AuthToken from headers
    authToken = headers['AuthToken']
    
    try:
        #Decode it with base64
        decoded_token = base64.b64decode(authToken)
        
        #Load with cPickle to token object
        token_object = cPickle.loads(decoded_token)
        
        #Check if the token is valid
        if not token_object.is_valid():
            return None
            
        #Return the data in token object if it is valid
        return token_object.data
    
    except (cPickle.UnpicklingError, base64.binascii.Error, AttributeError):
        # Catch exceptions related to unpickling or decoding errors, and invalid token objects
        return None