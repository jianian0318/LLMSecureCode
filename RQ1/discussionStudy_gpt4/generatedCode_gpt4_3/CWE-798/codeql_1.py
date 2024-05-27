from django.http import HttpResponse
from django.shortcuts import redirect


def process_request(request):
    '''
    Retrieve the "password"  from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    expected_password = "expected_value"    # replace it with the expected password
    password = request.GET.get('password')

    if password == expected_password:
        return redirect('login')    # this "login" refers to the name of the url that redirects to the login page
    else:
        return HttpResponse('Invalid password')  # response if password does not match the expected value.