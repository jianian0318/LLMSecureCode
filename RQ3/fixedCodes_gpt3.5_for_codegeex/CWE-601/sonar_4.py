from django.http import HttpResponseRedirect, HttpResponse


def set_location_header(request):
    '''
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    '''
    next_url = request.GET.get('next')
    if next_url:
        # Check if the next_url is a valid URL
        if not is_safe_url(url=next_url, allowed_hosts=request.get_host()):
            return HttpResponse('Invalid "next" value provided.')

        return HttpResponseRedirect(next_url)
    else:
        return HttpResponse('No "next" value provided.')