from django.http import HttpResponse
from django.shortcuts import redirect


def process_request(request):
    password = request.GET.get('password')  # Retrieve the "password" from the GET request

    # Compare the password to the expected value
    if password == None:
        return HttpResponse('Please provide a password', status=400)

    # Make the password check case-insensitive
    if password.lower() == "password123":
        return redirect('/login')  # Redirect to the login page
    else:
        return HttpResponse('Incorrect password', status=400)