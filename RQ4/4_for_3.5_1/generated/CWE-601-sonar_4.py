from django.http import HttpResponseRedirect


def set_location_header(request):
    '''
    Get the "next" value from the request and redirect to it using the 'Location' header.
    '''

    # Get the "next" value from the request
    next_url = request.GET.get('next')
    
    # Check if the "next" value exists
    if next_url:
        
        # Redirect to the "next" URL using the 'Location' header
        response = HttpResponseRedirect(next_url)

        # Set the 'Location' header
        response['Location'] = next_url

        return response
    
    # Return a 400 Bad Request response if "next" value does not exist
    return HttpResponse(status=400)