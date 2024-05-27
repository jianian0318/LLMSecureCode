from defusedxml.ElementTree import parse
from io import StringIO

from django.http import HttpResponse


def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    '''
    xpath = request.GET.get('xpath')
    xml = request.GET.get('xml')

    if not xpath or not xml:
        return HttpResponse("Missing required parameters", status=400)

    try:
        xml_payload = StringIO(xml)
        xml_tree = parse(xml_payload)
        result = xml_tree.xpath(xpath)
        return HttpResponse(result, status=200)
    except Exception:
        return HttpResponse("An error occured", status=500)
        