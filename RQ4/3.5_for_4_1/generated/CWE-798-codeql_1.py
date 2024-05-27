from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password')

    # The expected password. This is just an example, in real application this value should be stored securely and hashed.
    expected_password = get_expected_password()  # retrieve the expected password from a secure source

    if password == expected_password:
        # If the password is the same as the expected value, redirect to the login page
        return redirect('login')
    else:
        return HttpResponse("Incorrect password")