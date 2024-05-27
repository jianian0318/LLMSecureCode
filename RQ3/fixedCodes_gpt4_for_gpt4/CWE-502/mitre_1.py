import _pickle as cPickle
import base64
import io
from typing import Optional, Dict

def safe_deserialize(data: bytes) -> Optional[Dict[str, str]]:
    """
    This function aims to safely deserialize pickle data. 
    If the data is a dict object, it returns the dict, else returns None.
    """
    try:
        obj = cPickle.load(io.BytesIO(data))
        if isinstance(obj, dict):
            return obj
        else:
            raise ValueError("Unsafe pickle data; not a dict object")
    except Exception as e:
        print(f'Safe deserialization failed, reason: {str(e)}')
        return None

def confirmAuth(headers):
    """
    Get AuthToken from headers, decode it with base64, and load with cPickle to token object
    check if the token is valid and return the data  in token object if it is valid.
    """
    token = headers.get('AuthToken')
    if token:
        try:
            # decode base64 encoding
            token = base64.b64decode(token)
            # safe deserialization with cPickle
            tokenObj = safe_deserialize(token)
            if tokenObj is None:
                return None
        except (TypeError, cPickle.UnpicklingError, base64.binascii.Error) as e:
            return None

        # check the token validity
        # you could implement your own token validation logic here
        if 'expiry' in tokenObj and 'username' in tokenObj:
            return tokenObj   # return the data in token object
        else:
            return None

    return None


