from django.http import HttpResponseRedirect

def http_responser_redirect(request, url):
    '''
    Get the target url from the request and redirect to it
    '''
    return HttpResponseRedirect(url)