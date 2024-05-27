from django.http import HttpResponseRedirect
from urllib.parse import urlparse

def is_safe_url(url, allowed_hosts):
    '''
    Check if url is safe for redirection.
    '''
    url_info = urlparse(url)
    if url_info.netloc and url_info.netloc not in allowed_hosts:
        return False
    return True

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    target_url = request.GET.get('url', '/')
    if target_url and is_safe_url(target_url, request.get_host()):
        return HttpResponseRedirect(target_url)
    else:
        return HttpResponseRedirect('/')