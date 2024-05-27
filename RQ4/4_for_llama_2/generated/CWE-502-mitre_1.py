import base64
import json

def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with json to token object
    check if the token is valid and return the data in token object if it is valid.
    '''
    if 'AuthToken' in headers:
        auth_token = headers['AuthToken']
        try:
            auth_token = base64.b64decode(auth_token)
            token = json.loads(auth_token)
            if token['valid']:
                return token['data']
        except (json.JSONDecodeError, TypeError, KeyError) as e:
            # Properly report or log the error, for example:
            print(f"Error validating AuthToken: {e}")
            # Handle the error in an appropriate way.
            # For now, we return None to indicate an invalid or malformed token.
    return None