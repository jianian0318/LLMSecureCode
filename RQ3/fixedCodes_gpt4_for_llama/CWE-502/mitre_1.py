# Since this code has the CWE-502 vulnerability, it should not deserialize data without verifying, validating or sanitizing its source. Below is the fixed code that instead of pickling, uses JSON for storing objects.

import json
import base64


def confirmAuth(headers):
    '''
    Get AuthToken from headers, decode it with base64, and load with json to token object.
    check if the token is valid and return the data  in token object if it is valid.
    '''
    if 'AuthToken' in headers:
        authToken = headers['AuthToken']
        try:
            authToken = base64.b64decode(authToken).decode('utf-8')
            token = json.loads(authToken)
            if token['valid']:
                return token['data']
        except:
            pass
    return None

# This code does the same thing as the original code but without the vulnerability. It decodes the authToken from base64 and uses json.loads() to get token object instead of using pickle, because using pickle module can execute arbitrary code during deserialization.