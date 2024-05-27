from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next_value = request.GET.get('next')
    return redirect(next_value)