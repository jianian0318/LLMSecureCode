from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    # get the target URL from the request
    target_url = request.GET.get('target')
    
    # check if target URL exists in the request, if not default to home
    if not target_url:
        target_url = '/'

    # use HttpResponseRedirect to redirect to the target_url
    return HttpResponseRedirect(target_url)