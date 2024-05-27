from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    target_url = request.GET.get('url')
    return HttpResponseRedirect(target_url)