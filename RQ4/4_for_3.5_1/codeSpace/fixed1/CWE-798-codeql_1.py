import os
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password', '')
    username = "your_username"  # Replace with real username

    # Use Django's built-in authentication system
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # If authentication is successful, redirect to the desired page
        return redirect('/home')
    else:
        return HttpResponse('Invalid password')