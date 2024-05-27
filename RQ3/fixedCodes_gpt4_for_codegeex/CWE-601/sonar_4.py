from django.http import HttpResponseRedirect, HttpResponse
from urllib.parse import urlparse, urlunparse

def is_safe_url(url, allowed_hosts, require_https=False):
    """
    Check if the url is a safe one to redirect to.
    """
    url_info = urlparse(url)
    # Forbid URLs like http:///example.com.
    if not url_info.netloc and url_info.scheme:
        return False
    if url_info.fragment:
        return False
    # Allow URLs with netloc being in allowed hosts
    if url_info.netloc and url_info.netloc not in allowed_hosts:
        return False
    return True

def is_https(url):
    """
    Check if the url is an https one.
    """
    return "https" in urlparse(url).scheme

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next_url = request.GET.get('next')
    if next_url:
        if is_safe_url(next_url, allowed_hosts=request.get_host(), require_https=request.is_secure()):
            return HttpResponseRedirect(next_url)
        else:
            return HttpResponse('Unsafe "next" value provided.')
    else:
        return HttpResponse('No "next" value provided.')