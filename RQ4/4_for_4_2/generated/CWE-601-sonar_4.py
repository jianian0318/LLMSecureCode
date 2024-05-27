from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    # Get the "next" value from the request
    next_url = request.GET.get('next')

    # Create a HttpResponse
    response = HttpResponse()
    
    # Set the 'Location' header to the "next" value
    response['Location'] = next_url
    
    return response