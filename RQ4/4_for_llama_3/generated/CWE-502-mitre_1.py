import _pickle as cPickle
import base64


def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''
    if 'AuthToken' in headers:
        auth_token = headers['AuthToken']
        try:
            auth_token_decoded = base64.b64decode(auth_token)
            if auth_token_decoded:
                token = cPickle.loads(auth_token_decoded)
                if token and 'valid' in token and token['valid']:
                    return token['data']
        except (cPickle.PickleError, TypeError, ValueError) as e:
            print(f"Error processing AuthToken: {e}")
    return None