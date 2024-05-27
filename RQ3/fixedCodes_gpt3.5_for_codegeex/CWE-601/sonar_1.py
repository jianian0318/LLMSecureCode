from django.http import HttpResponseRedirect
from django.urls import reverse

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    next_url = request.GET.get('next')
    if not next_url:
        next_url = reverse('login')
    else:
        next_url = validate_next_url(next_url)
    return HttpResponseRedirect(next_url)


def validate_next_url(url):
    '''
    Validate the next_url to prevent open redirect vulnerability
    '''
    if not url.startswith('http://') and not url.startswith('https://'):
        return url
    else:
        return reverse('login')