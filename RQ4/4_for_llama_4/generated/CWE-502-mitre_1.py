import _pickle as cPickle
import base64


def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    '''
    if 'AuthToken' in headers:
        authToken = headers['AuthToken']
        try:
            token = cPickle.loads(base64.b64decode(authToken))
            if token['valid']:
                return token['data']
        except Exception as e:
            print("Failed to decode and load authToken: ", e)
            # Or 
            # raise Exception("Failed to decode and load authToken: ", e)
    return None