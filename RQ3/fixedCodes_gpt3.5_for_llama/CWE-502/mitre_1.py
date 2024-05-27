import _pickle as cPickle
import base64


def confirmAuth(headers):
    if 'AuthToken' in headers:
        authToken = headers['AuthToken']
        try:
            authToken = base64.b64decode(authToken)
            token = cPickle.loads(authToken)
            if "valid" in token and token['valid']:
                return token['data']
        except:
            pass
    return None