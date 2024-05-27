from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url

def http_responser_redirect(request):
    '''
    Get the target URL from the request and redirect to it only if it's safe 
    '''
    target_url = request.GET.get('target_url')

    # Check if the URL is safe for redirection
    if is_safe_url(
        url=target_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return HttpResponseRedirect(target_url)
    else:
        return HttpResponseRedirect('/')