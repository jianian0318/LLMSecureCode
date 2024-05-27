from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    if request.method == 'GET':
        if 'password' in request.GET:
            password = request.GET['password']
        else:
            password = None

        if password and authenticate(password):
            return redirect('/login/')

    return HttpResponse("Unauthorized", status=401)

def authenticate(password):
    # Compare the password to the expected value securely
    expected_password = "mypassword"
    return password == expected_password