from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next_val = request.GET.get('next', '/')

    # Using HttpResponseRedirect to redirect based on the 'next' value
    response = HttpResponseRedirect(next_val)

    return response