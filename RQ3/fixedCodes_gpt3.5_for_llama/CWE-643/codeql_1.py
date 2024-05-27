from lxml import etree
from io import StringIO

from django.http import HttpResponse

def xpath_query(request):
    xpath = request.GET.get('xpath')
    xml = request.GET.get('xml')

    if not xpath or not xml:
        return HttpResponse("Missing required parameters", status=400)

    try:
        xpath = "/tag[@id='{}']".format(xpath)
        xml_tree = etree.parse(StringIO(xml))
        result = xml_tree.xpath(xpath)
        return HttpResponse(str(result), status=200)
    except Exception as e:
        return HttpResponse(str(e), status=500)