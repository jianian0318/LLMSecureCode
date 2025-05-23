from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next = request.GET.get('next', None)
    if next is not None:
        response = HttpResponse()
        response['Location'] = next
        return response
    return HttpResponseRedirect('/')