import _pickle as cPickle
import base64

class InvalidTokenException(Exception):
    pass

def confirmAuth(headers):
    if 'AuthToken' not in headers:
        raise InvalidTokenException("AuthToken not in headers")

    authToken = headers['AuthToken']
    
    try:
        token_obj_bytes = base64.b64decode(authToken)
        token_obj = cPickle.loads(token_obj_bytes)
    except Exception:
        raise InvalidTokenException("Invalid AuthToken")

    if not token_obj.valid():
        raise InvalidTokenException("Invalid AuthToken")

    return token_obj.data