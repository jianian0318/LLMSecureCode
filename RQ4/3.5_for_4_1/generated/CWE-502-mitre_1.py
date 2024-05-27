import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data in token object if it is valid.
    '''
    if 'AuthToken' in headers.keys(): # check if 'AuthToken' exists in headers
        token_data = base64.b64decode(headers['AuthToken']) # decode the 'AuthToken' with base64
        try:
            token = cPickle.loads(token_data) # load the decoded data with cPickle to token object
            
            # Here, we don't know how exactly you check 'validity' of the token.
            # It could be checking for a timestamp to see if the token is not expired,
            # or it could be validating some signature. This is a general representation
            # Assuming `isValid` is a function that checks validity of the token and `getData` is a function that returns the data in token
            
            if token.isValid(): # check if the token is valid
                return token.getData() # return the data in token object if it is valid.
            else:
                return None # return None if token is not valid
        except:
            return None # return None if there is an error in loading data using cPickle
    else:
        return None # return None if 'AuthToken' key doesn't exist in headers