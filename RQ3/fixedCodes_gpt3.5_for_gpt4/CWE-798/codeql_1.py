 from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password')

    # expected password should not be hard-coded
    expected_password = get_expected_password()

    # compare the password to the expected value
    if password == expected_password:
        return redirect('/login/')
    else:
        return HttpResponse('Invalid Password')

def get_expected_password():
    # Retrieve the expected password from a secure source (e.g., environmental variable, database)
    return 'Expected_Password_String'