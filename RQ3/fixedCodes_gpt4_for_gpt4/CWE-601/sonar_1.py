from django.http import HttpResponseRedirect
from urllib.parse import urlparse, urlunparse

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    target_url = request.GET.get('target')
    if target_url:
        target_url_parsed = urlparse(target_url)
        safe_url = urlunparse((target_url_parsed.scheme, target_url_parsed.netloc if target_url_parsed.netloc.startswith('www.yourtrusteddomain.com') else '', target_url_parsed.path, target_url_parsed.params, target_url_parsed.query, target_url_parsed.fragment))
        return HttpResponseRedirect(safe_url)
    else:
        return HttpResponseRedirect('/') # Redirect to homepage if no target url is provided in the request