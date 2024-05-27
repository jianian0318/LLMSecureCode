from django.http import HttpResponseRedirect, HttpResponse
from django.utils.http import is_safe_url
from django.conf import settings

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect to it using the 'Location' header,
    after validating that the URL is safe.
    '''
    next_url = request.GET.get('next', '/')
    # Ensure the URL is safe to redirect to
    if not is_safe_url(url=next_url, allowed_hosts=settings.ALLOWED_HOSTS):
        next_url = '/'
    # Redirect
    response = HttpResponse(status=302)
    response['Location'] = next_url
    return response

# This code ensures that the 'next' parameter is a safe URL by using Django's built-in `is_safe_url` method. The `allowed_hosts` should be set in the Django settings for your project, and the `next_url` should default to the homepage ('/') if no safe URL is provided. The `HttpResponseRedirect` is replaced with a manual setting of the 302 HTTP status in a plain `HttpResponse` to make it explicit.