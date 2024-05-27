from django.http import HttpResponse
from django.shortcuts import redirect


def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password', '')
    
    # Compare the password to the expected value
    expected_password = 'password123'
    
    # If the password is the same, redirect to the login page
    if password == expected_password:
        return redirect('login')
    else:
        return HttpResponse('Invalid password')