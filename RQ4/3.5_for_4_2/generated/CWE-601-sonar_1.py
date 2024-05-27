from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    target_url = request.GET.get('target')
    if target_url:
        return HttpResponseRedirect(target_url)
    else:
        # Return a response to indicate that target_url is not provided
        return HttpResponseRedirect('/')