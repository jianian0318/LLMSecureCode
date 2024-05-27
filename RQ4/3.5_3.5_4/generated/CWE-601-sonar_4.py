from django.http import HttpResponseRedirect


def set_location_header(request):
    next_url = request.GET.get('next')
    if next_url:
        return HttpResponseRedirect(next_url)
    else:
        return HttpResponse('next URL not found')