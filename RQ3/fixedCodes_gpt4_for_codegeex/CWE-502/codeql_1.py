import django.core.signing
from django.conf.urls import url

def getSignedData(signed_data):
    '''
    Return deserialized safe data
    '''
    deserialized_safe_data = django.core.signing.loads(signed_data)
    return deserialized_safe_data

urlpatterns = [
    url(r'^get_data$', getSignedData, name='get_signed_data'),
]