from lxml import etree
from io import StringIO
from django.http import HttpResponse


def xpath_query(request):
    xpath = request.GET.get('xpath')
    xml = request.GET.get('xml')

    root = etree.parse(StringIO(xml))
    result = root.xpath("/tag[@id={}]".format(xpath))
    
    return HttpResponse(result)