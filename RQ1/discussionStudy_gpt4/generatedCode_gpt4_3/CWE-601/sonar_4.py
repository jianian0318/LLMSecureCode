from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next = request.GET.get('next')
    if next is not None:
        response = HttpResponse(status=302)
        response['Location'] = next
        return response
    else:
        return HttpResponseRedirect('/') # return to home if 'next' does not exist