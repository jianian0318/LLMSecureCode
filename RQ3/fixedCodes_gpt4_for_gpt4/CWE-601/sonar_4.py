from django.http import HttpResponseRedirect, HttpResponse
from urllib.parse import urlparse
from django.contrib.sites.models import Site

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next = request.GET.get('next', '')
    url_is_safe = is_safe_url(
        url=next,
        allowed_hosts={Site.objects.get_current().domain},
        require_https=request.is_secure(),
    )
    if not url_is_safe:
        return HttpResponse("URL not allowed", status=400)
    response = HttpResponse(status=302)
    response['Location'] = next
    return response

def is_safe_url(url, allowed_hosts, require_https=True):
    url_info = urlparse(url)
    if url_info.scheme not in ('http', 'https') and require_https:
        return False
    if url_info.netloc and url_info.netloc not in allowed_hosts:
        return False
    return True