from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    # From the request get the target url. Assume it's stored in request.POST['target_url']
    target_url = request.POST.get('target_url')
    
    # Redirect to the target url
    return HttpResponseRedirect(target_url)