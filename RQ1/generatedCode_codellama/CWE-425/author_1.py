from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def getResource(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')
        file_path = f'/path/to/files/{username}/{date}/file.txt'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        else:
            return render(request, 'error.html', {'error': 'File not found'})
    else:
        return render(request, 'error.html', {'error': 'Invalid request'})
