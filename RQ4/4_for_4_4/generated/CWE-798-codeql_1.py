import os
from django.http import HttpResponse
from django.shortcuts import redirect


def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password', None)

    # Get an expected password from environment variables
    expected_password = os.environ.get('EXPECTED_PASSWORD')

    # Compare the password to the expected value
    if password == expected_password:
        # If it is the same, redirect to the login page
        return redirect('/login/')
    
    # If not the same, you could return a response saying invalid password or 
    # redirect to some other page, this up to how the logic should be. 
    # For example:
    return HttpResponse('Invalid password')