from django.http import HttpResponseRedirect

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next_url = request.GET.get('next', '/')  # Get the value of 'next' from the request's GET parameters
    return HttpResponseRedirect(next_url)  # Redirect to the URL retrieved from 'next'