from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    # Get the target url from the request
    target_url = request.GET.get('url', '/')  # Default to root if no url parameter is provided

    # Redirect to the target url
    return HttpResponseRedirect(target_url)