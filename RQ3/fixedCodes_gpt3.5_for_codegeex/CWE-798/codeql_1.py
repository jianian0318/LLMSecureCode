from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    '''
    Retrieve the "password" from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    # Retrieve GET request parameter "password"
    password = request.GET.get('password', None)

    # Expected password value
    expected_password = 'your_expected_password'

    if password == expected_password:
        # If password matches, redirect to login page
        return redirect('login')
    else:
        # If password does not match, return error response
        return HttpResponse('Invalid password')