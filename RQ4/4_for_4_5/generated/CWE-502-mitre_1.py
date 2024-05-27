import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''
    # Get AuthToken from headers
    token_b64 = headers.get('AuthToken', None)

    if token_b64 is not None:
        try:
            # Decode it with base64
            token_pickle = base64.b64decode(token_b64)

            # Load with cPickle to token object
            token = cPickle.loads(token_pickle)

            # Check validity of token
            # In actual implementation, this could be implemented differently based on your authentication/authorization system's requirements. For simplicity, we're just making sure it's not null or empty here.
            if token:  
                return token
            else:
                return "Invalid token"

        except Exception as e:
            return str(e)  # Return exception message

    else:
        return "AuthToken is not provided"