from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password')

    # Compare the password to the expected value
    if password == get_expected_password():
        # If it is the same, redirect to the login page.
        return redirect('login_page_url')
    else:
        return HttpResponse('Invalid password')

def get_expected_password():
    # In a secure implementation, the expected password should not be hardcoded.
    # Instead, it should be stored securely, such as in a database or environment variable.
    # For the purpose of this example, we will assume it is stored in an environment variable called "EXPECTED_PASSWORD".
    import os
    expected_password = os.environ.get('EXPECTED_PASSWORD')

    return expected_password