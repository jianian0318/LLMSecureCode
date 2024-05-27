import os
import pickle

class Payload(object):
    def __reduce__(self):
        return os.system, ('ls',)

def makePickleData(payload: Payload):
    return pickle.dumps(payload)

# To fix the vulnerability associated with the pickle module,
# we need to prevent code execution from unpickling untrusted data.
# One way to do this is by using a whitelist of allowed classes that can be unpickled.
# In this case, we can define a helper function that checks if a class is allowed to be unpickled.

def is_allowed_class(cls):
    # Define your own whitelist of allowed classes here
    allowed_classes = {Payload}
    return cls in allowed_classes

def unpickleData(data):
    try:
        obj = pickle.loads(data)
        if not is_allowed_class(type(obj)):
            raise ValueError('Class is not allowed')
        return obj
    except (ValueError, pickle.UnpicklingError) as e:
        print('Error: {}'.format(str(e)))
        return None

# Example usage:
payload = Payload()
pickle_data = makePickleData(payload)
unpickled_obj = unpickleData(pickle_data)
print(unpickled_obj)