from django.http import HttpResponse
from django.shortcuts import redirect


def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password')

    # expected password
    expected_password = 'Expected_Password_String'

    # compare the password to the expected value
    if password == expected_password:
        # if it is the same, redirect to the login page.
        return redirect('/login/')
    else:
        return HttpResponse('Invalid Password')