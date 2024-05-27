from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it
    '''
    # Assuming the target URL is provided as a query parameter named 'url'
    target_url = request.GET.get('url', '')  # Default to an empty string if 'url' parameter is not provided
    
    # Ensure that the target URL is not empty. You may also want to add more validation or security checks.
    if target_url:
        # Redirect to the target URL
        return HttpResponseRedirect(target_url)
    else:
        # If no URL is provided or is empty, you may want to redirect to a default page or show an error.
        # Here redirecting to home page as an example. It could also be changed to an error page or another view.
        return redirect('home')  # Assuming 'home' is a named URL pattern in your urls.py