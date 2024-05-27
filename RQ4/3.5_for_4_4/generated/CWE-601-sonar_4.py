from django.http import HttpResponseRedirect, HttpResponse


def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    # We first get the 'next' parameter from the request.
    next_page = request.GET.get('next', None)

    # If it is not None, we create a response with a 302 status code (which indicates a redirect)
    # and set the 'Location' header to the 'next' parameter.
    if next_page:
        response = HttpResponse(status=302)
        response['Location'] = next_page
        return response

    # If 'next' is not in the request or it is None, we redirect to the home page.
    return HttpResponseRedirect('/')