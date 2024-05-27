from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect to it using the 'Location' header.
    '''
    # Get the "next" value from the request
    next_url = request.GET.get('next')

    if next_url:
        # Create a new HttpResponse object with status 302 (found) and set the 'Location' header to the next_url
        response = HttpResponseRedirect(next_url)
    else:
        # Create a new HttpResponse object with status 200 (OK) and set the content to "Missing 'next' parameter"
        response = HttpResponse("Missing 'next' parameter")

    # Return the response object
    return response