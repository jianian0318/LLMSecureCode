from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    # Get the redirect_url value from the request's GET data
    redirect_url = request.GET.get('redirect_url', '/')
    # Use HttpResponseRedirect to redirect to the obtained URL
    return HttpResponseRedirect(redirect_url)