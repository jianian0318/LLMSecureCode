import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''

    # Extract the AuthToken from headers
    if 'AuthToken' in headers:
        encoded_token = headers['AuthToken']
    else:
        return None
        
    # Decode the token with base64
    decoded_token = base64.b64decode(encoded_token)
    
    # Load the token to a Python object with cPickle
    try:
        token_object = cPickle.loads(decoded_token)
    except Exception as e:
        print('Error while loading token: ', e)
        return None

    # Assume there is a function called is_token_valid that checks the validity of the token
    # Since the implementation of token validation is not specified, it's just a placeholder here.
    # Replace it with actual validation logic.
    if is_token_valid(token_object):
        return token_object

    return None

# Define the placeholder function is_token_valid(), it should be replaced with actual implementation
def is_token_valid(token):
    # Placeholder for token validation logic
    return True