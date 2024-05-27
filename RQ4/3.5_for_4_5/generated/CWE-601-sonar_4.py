from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next_url = request.GET.get('next')
    
    if next_url is None:
        # If 'next' does not exist, then return a simple HttpResponse
        return HttpResponse()

    # If 'next' exists, then redirect to that URL using the 'Location header'
    response = HttpResponseRedirect(next_url)
    
    return response