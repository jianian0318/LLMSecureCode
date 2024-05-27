from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it.
    '''
    # Get target URL from request
    target_url = request.POST.get('target_url')

    # Redirect to target URL
    return HttpResponseRedirect(target_url)