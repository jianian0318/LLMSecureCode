import os
from django.http import HttpResponse
from django.shortcuts import redirect

def get_secret_password():
    # Get the secret password from an environment variable
    # Ensure to set this environment variable outside the application's code,
    # for example, in a separate configuration file or a secure secrets management service.
    return os.environ.get('MYAPP_SECRET_PASSWORD', 'default_password')

def process_request(request):
    '''
    Retrieve the "password" from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    password = request.GET.get('password')
    secret_password = get_secret_password()
    if password == secret_password:
        return redirect('/login/')
    else:
        return HttpResponse('Invalid password')

# Additional setup may be required:
# For example, to set an environment variable in Linux or macOS:
# export MYAPP_SECRET_PASSWORD='TheActualSecretPassword'

# Or in Windows:
# set MYAPP_SECRET_PASSWORD=TheActualSecretPassword