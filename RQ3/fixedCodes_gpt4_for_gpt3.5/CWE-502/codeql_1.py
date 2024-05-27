# Since it's not possible to guarantee that the deserialization process will be secure with pickle library, we can use json library instead to make the data exchange more secure.

from django.conf.urls import url
import json


def getData(serialized):
    '''
    Return deserialized data
    '''

    data = json.loads(serialized)
    return data

# This version of code is safe because JSON deserialization is not capable of executing potential harmful operations like pickle does. Make sure that your expected input is always in JSON format, or else, this will break.