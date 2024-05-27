from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    # Assuming 'redirect_to' is the key of the target URL in request
    target_url = request.GET.get('redirect_to')
    
    # Validate if the target_url exists, if not it will redirect to some default url
    if not target_url:
        target_url = '/default-url-to-redirect-if-no-param/'
    
    # Return http redirect response 
    return HttpResponseRedirect(target_url)