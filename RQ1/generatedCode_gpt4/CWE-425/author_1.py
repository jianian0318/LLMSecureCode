from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def getResource(request):
    '''
    Get username and date from the request, then
    send the file to the user by creating path by the username and date.
    '''
    if request.method == 'POST':
        # Get username and date from the request
        username = request.POST.get('username')
        date = request.POST.get('date')

        # Create a path using username and date
        file_path = os.path.join(username, date)

        # Ensure the file exists before sending
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename={}'.format(os.path.basename(file_path))
                
        else:
            response = HttpResponse('File does not exist!')
        
        return response
        
    else:
        return HttpResponse('Invalid request method!')