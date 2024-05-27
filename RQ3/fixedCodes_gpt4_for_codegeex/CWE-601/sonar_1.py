from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlparse

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    next_url = request.GET.get('next')
    if not next_url:
        next_url = reverse('login')
    else:
        netloc = urlparse(next_url).netloc
        if netloc and netloc != request.get_host():
            next_url = reverse('login')    
    return HttpResponseRedirect(next_url)