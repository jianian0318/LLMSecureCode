def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    # Get the target url from the request
    target_url = request.GET.get('url', '/')  # default to root ('/') if url is not provided in the request

    # Redirect to the target url
    return HttpResponseRedirect(target_url)