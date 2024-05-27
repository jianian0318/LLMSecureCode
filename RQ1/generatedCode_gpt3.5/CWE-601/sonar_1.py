from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    Get the target URL from the request and redirect to it
    '''
    target_url = request.GET.get('target_url')
    return HttpResponseRedirect(target_url)