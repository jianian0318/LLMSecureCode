from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password')

    # Compare the password to the expected value
    expected_password = 'mypassword'

    if password == expected_password:
        # If the passwords match, redirect to the login page
        return redirect('/login/')
    else:
        # If the passwords don't match, return an HttpResponse with an error message
        return HttpResponse('Invalid password')