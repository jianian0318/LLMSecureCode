import os
from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password', '')
    
    # Retrieving the expected password from environment variables
    expected_password = os.environ.get('EXPECTED_PASSWORD', '')
    
    # If the password is the same, redirect to the login page
    if password == expected_password and expected_password != '':
        return redirect('login')
    else:
        return HttpResponse('Invalid password')