from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings

def process_request(request):
    password = request.GET.get('password')
    expected_password = settings.EXPECTED_PASSWORD

    if password == expected_password:
        return redirect('/login')

    return HttpResponse('Invalid password')

# Add this to your Django settings.py
# Remember to change the password and never hard-code it
EXPECTED_PASSWORD = 'your_password'