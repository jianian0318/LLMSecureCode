from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    # Get the "next" parameter from the request
    next_url = request.GET.get('next', '')

    # If there's no "next" parameter, return an error response
    if not next_url:
        return HttpResponse('No "next" parameter found')

    # Create a response object
    response = HttpResponseRedirect('/')

    # Set the Location header to the "next" URL
    response['Location'] = next_url

    return response