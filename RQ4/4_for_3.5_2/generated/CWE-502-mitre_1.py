import _pickle as cPickle
import base64

def confirmAuth(headers):
    # Get AuthToken from headers
    auth_token = headers.get("AuthToken")

    # Check if auth_token exists
    if auth_token:
        # Decode auth_token with base64
        decoded_token = base64.b64decode(auth_token)
        
        # Load decoded_token with cPickle to token object
        token = cPickle.loads(decoded_token)

        # Check if the token is valid
        if token.get("valid"):
            # Return the data in token object if it is valid
            return token.get("data")
    
    return None