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
            authToken = base64.b64decode(authToken)
            token = cPickle.loads(authToken)
            if token['valid']:
                return token['data']
        except:
            pass
    return None
