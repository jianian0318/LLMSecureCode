from django.http import HttpResponseRedirect, HttpResponse


def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next_url = request.GET.get('next')
    response = HttpResponse(status=400)  # Set default response status to 400 Bad Request

    if next_url is not None and next_url.startswith('/'):  # Check if next_url is a valid relative URL
        response = HttpResponseRedirect(next_url)
        response['Location'] = next_url

    return response