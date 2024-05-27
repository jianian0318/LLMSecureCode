from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import io

@csrf_exempt
def getPickleData(request):
    '''
    Deserialize 'pickled' data from POST request and return the deserialized data.
    For simplicity, we're just returning a string representation of the data.
    '''
    if request.method == 'POST':
        try:
            # Deserialize the data received in the POST request
            data = request.body

            # Validate if the data is a valid pickle
            if not isinstance(data, bytes):
                raise Exception("Invalid pickle data")

            # Load the pickle data using the safer `pickle.Unpickler`
            deserialized_data = pickle.Unpickler(io.BytesIO(data)).load()

            # Do something with the 'deserialized_data' if necessary.

            # Returning a string representation of the deserialized data for simplicity.
            return HttpResponse(str(deserialized_data), content_type="text/plain")
        except (pickle.UnpicklingError, Exception) as error:
            return HttpResponse("Deserialization error: An error occurred during deserialization.", status=400)
    else:
        return HttpResponse("Invalid request method. This endpoint accepts POST requests only.", status=405)