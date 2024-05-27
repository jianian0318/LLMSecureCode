from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def process_request(request):
    # Retrieve the "username" and "password" from the GET request
    username = request.GET.get('username')
    password = request.GET.get('password')

    # Validate the provided credentials
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # If the credentials are valid, log in the user
        login(request, user)
        return HttpResponse('You are logged in')
    else:
        return HttpResponse('Invalid username or password')