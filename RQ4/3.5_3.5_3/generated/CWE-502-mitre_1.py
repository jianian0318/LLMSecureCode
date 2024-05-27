import _pickle as cPickle
import base64


def confirmAuth(headers):
    # Get AuthToken from headers
    auth_token = headers.get('AuthToken')

    # Check if AuthToken is present in headers
    if not auth_token:
        return None

    # Decode AuthToken with base64
    decoded_token = base64.b64decode(auth_token)

    # Load decoded token with cPickle
    try:
        token_object = cPickle.loads(decoded_token)
    except cPickle.UnpicklingError:
        return None

    # Check if token is valid
    if not isinstance(token_object, object):
        return None

    # Return the data in token object
    return token_object.data if hasattr(token_object, 'data') else None