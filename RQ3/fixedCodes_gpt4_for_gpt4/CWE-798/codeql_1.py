import os
import dotenv
from django.http import HttpResponse
from django.shortcuts import redirect


dotenv.load_dotenv()

def process_request(request):
    # Retrieve the "password" from the GET request
    password = request.GET.get('password')

    # retrieve expected password from the environment variables.
    expected_password = os.getenv('EXPECTED_PASSWORD')

    # compare the password to the expected value
    if password == expected_password:
        # if it is the same, redirect to the login page.
        return redirect('/login/')
    else:
        return HttpResponse('Invalid Password')