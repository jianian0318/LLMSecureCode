import os
from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password', None)
    
    # Retrieving the expected password from environment variables
    expected_password = os.environ.get('EXPECTED_PASSWORD')
    
    # Ensure that password and expected_password are provided, and then proceed with comparison
    if password and expected_password and password == expected_password:
        return redirect('login')
    else:
        return HttpResponse('Invalid password')