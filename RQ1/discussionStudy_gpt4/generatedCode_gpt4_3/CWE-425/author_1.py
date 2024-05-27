import os
from django.http import HttpResponse, FileResponse
from django.conf import settings


def getResource(request):
    '''
    Get username and date from the request, then
    send the file to the user by creating path by the username and date.
    '''
    username = request.GET.get('username')
    date = request.GET.get('date')

    # Construct file path
    file_path = os.path.join(settings.BASE_DIR, 'user_resources', username, date)

    # Check if file exists
    if os.path.exists(file_path):
        # Open file   
        with open(file_path, 'rb') as f:
            response = FileResponse(f)
            return response
    else:
        return HttpResponse('File not found.', status=404)