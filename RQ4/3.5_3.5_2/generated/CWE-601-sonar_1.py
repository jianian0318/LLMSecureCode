def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    target_url = request.GET.get('target_url')
    if target_url:  # Check if target_url is not empty
        return HttpResponseRedirect(target_url)
    else:
        return HttpResponseRedirect('/')  # Redirect to a default URL if target_url is not provided or empty