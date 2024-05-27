from django.shortcuts import redirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    target_url = request.GET.get('url')     # Get the target url from the request parameters

    return redirect(target_url)             # Redirect to the target url