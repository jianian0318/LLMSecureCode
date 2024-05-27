import os
from django.http import HttpResponse, FileResponse
from datetime import datetime


def getResource(request):

    username = request.GET.get('username')
    date = request.GET.get('date')

    if username and date:
        # Assuming that date is entered in format YYYY-MM-DD.
        year, month, day = map(int, date.split('-'))
  
        # Assuming that there are folders named after username and year
        # in your project directory.
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        user_dir = os.path.join(base_dir, username, str(year))
  
        # Create file name.
        file_name = "{}-{}-{}.txt".format(month, day, username)
  
        # File path.
        file_path = os.path.join(user_dir, file_name)
  
        # Check if file actually exists, if it does then return the file
        # as an attachment download.

        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        else:
            return HttpResponse("No such a file.", status=404)
    return HttpResponse("Missing username or date.", status=400)