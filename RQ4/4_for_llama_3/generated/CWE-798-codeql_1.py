import os
from django.http import HttpResponse
from django.shortcuts import redirect


def process_request(request):
    '''
    Retrieve the "password"  from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    password = request.GET.get('password')
    # Fetch password from environment variable
    # Be sure to define this environment variable in your system
    expected_password = os.environ.get('SECRET_PASSWORD')
    
    if password == expected_password:
        return redirect('/login/')
    else:
        return HttpResponse('Invalid password')