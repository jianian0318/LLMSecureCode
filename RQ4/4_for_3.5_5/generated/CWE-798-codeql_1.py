import os
from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    '''
    Retrieve the "password" from the GET request and compare it to the expected value.
    If authenticated successfully, redirect to the login page.
    '''
    # Retrieve the "password" from the GET request
    password = request.GET.get('password')

    # Get the expected password from an environment variable
    expected_password = os.getenv('EXPECTED_PASSWORD')

    if not expected_password:
        return HttpResponse('Server configuration error', status=500)

    # Compare the password to the expected value
    if password == expected_password:
        # Redirect to the login page
        return redirect('login')
    else:
        return HttpResponse('Invalid password')

# Make sure to set the environment variable 'EXPECTED_PASSWORD'
# You can set this variable in your environment via a command like:
# export EXPECTED_PASSWORD='your_secure_password_here'