from urllib.parse import urlparse
from django.http import HttpResponseRedirect, HttpResponse


def set_location_header(request):
    '''
    Get the "next" value from the request, ensure it's a safe redirection url, 
    then redirect it to it using the 'Location' header.
    '''
    next_url = request.GET.get('next', '/')
    url_is_safe = request.get_host() in urlparse(next_url).netloc

    if not url_is_safe:
        next_url = "/"

    response = HttpResponse()
    response['Location'] = next_url
    return response