from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next = request.GET.get('next', '')
    if not next:
        # If there is no 'next' parameter, return a HTTP 400 response
        return HttpResponse('Bad Request', status=400)
    response = HttpResponseRedirect(next)
    return response