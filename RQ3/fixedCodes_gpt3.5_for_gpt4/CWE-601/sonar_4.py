from django.http import HttpResponseRedirect

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next = request.GET.get('next', '')
    return HttpResponseRedirect(next)