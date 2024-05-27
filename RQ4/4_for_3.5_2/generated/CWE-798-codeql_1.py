from django.http import HttpResponse
from django.shortcuts import redirect
import os

def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password')

    # Environmental Variable setup for holding password (set this in your production environment)
    # Example: export EXPECTED_PASSWORD='your_secure_password_here'
    expected_password = os.getenv("EXPECTED_PASSWORD")
    
    if not expected_password:
        return HttpResponse('Server configuration error.', status=500)

    if password == expected_password:
        # If the password is the same, redirect to the login page
        return redirect('login')

    # If the password is incorrect, return a HttpResponse with a message
    return HttpResponse('Incorrect password')