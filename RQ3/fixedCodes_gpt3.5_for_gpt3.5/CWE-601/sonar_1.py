from django.http import HttpResponseRedirect
from urllib.parse import urlparse

def http_responser_redirect(request):
    '''
    Get the target URL from the request and redirect to it
    '''
    target_url = request.GET.get('target_url')
    
    if target_url and urlparse(target_url).netloc == "":
        return HttpResponseRedirect(target_url)
    
    return HttpResponseRedirect("/")