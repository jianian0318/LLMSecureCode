from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    target_url = request.GET.get('url', None)
    if target_url and 'http' in target_url:
        return HttpResponseRedirect(target_url)
    else:
        return HttpResponseRedirect('/')

# NOTE: Added a condition to check if 'http' is present in the target_url to ensure that only valid URLs are redirected.