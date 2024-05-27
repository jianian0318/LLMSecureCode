import os
from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password')

    # Expected password should be securely obtained from environment or a secure vault
    expected_password = os.getenv('EXPECTED_PASSWORD')

    if password == expected_password:
        # If the passwords match, redirect to the login page
        return redirect('/login/')
    else:
        # If the passwords don't match, return an HttpResponse with an error message
        return HttpResponse('Invalid password')