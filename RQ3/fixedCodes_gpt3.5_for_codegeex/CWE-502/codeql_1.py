from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    Return deserialized data
    '''
    try:
        deserialized_data = pickle.loads(pickled)
        return deserialized_data
    except pickle.UnpicklingError:
        return None

urlpatterns = [
    url(r'^get_data$', getPickleData, name='get_pickle_data'),
]