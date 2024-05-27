from django.http import HttpResponseRedirect, HttpResponse


def set_location_header(request):
    next_url = request.GET.get('next', '/')
    return HttpResponseRedirect(next_url)