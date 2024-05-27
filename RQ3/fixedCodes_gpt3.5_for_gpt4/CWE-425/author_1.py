from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def getResource(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')

        if username and date:
            # Validate provided username and date before creating a filepath
            if not any(char in "\\/:*?\"<>|" for char in username + date):
                # Create a path using username and date
                file_path = os.path.join(username, date)

                # Validate file path
                if os.path.exists(file_path) and os.path.isfile(file_path):
                    with open(file_path, 'rb') as file:
                        response = HttpResponse(file, content_type='application/octet-stream')
                        response['Content-Disposition'] = 'attachment; filename={}'.format(os.path.basename(file_path))
                else:
                    response = HttpResponse('File does not exist!')
            else:
                response = HttpResponse('Invalid characters in username or date!')
        else:
            response = HttpResponse('Username or date not provided!')
    else:
        response = HttpResponse('Invalid request method!')

    return response