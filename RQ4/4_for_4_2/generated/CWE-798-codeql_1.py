from django.http import HttpResponse
from django.shortcuts import redirect
import os


def process_request(request):
    '''
    Retrieve the "password" from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    # Retrieve password from GET request
    password = request.GET.get('password')
    
    # Expected password stored in Environment variable
    expected_password = os.environ.get('EXPECTED_PASSWORD')
    
    # Compare retrieved password with expected password
    if password == expected_password:
        # If password is correct, redirect to login page
        return redirect('login')  # Replace 'login' with your login page name
    else:
        return HttpResponse("Unauthorized", status=401)  