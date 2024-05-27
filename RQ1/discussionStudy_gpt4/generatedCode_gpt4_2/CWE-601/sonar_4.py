from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect to it using the 'Location' header.
    '''
    next_page = request.GET.get('next') # Get the "next" value from the request

    if next_page:
        response = HttpResponse(status=302)
        response['Location'] = next_page # Set the 'Location' header to next_page

        return response # Return the response

    return HttpResponse("No 'next' parameter in request.", status=400)