from defusedxml import DefusedXmlException
from defusedxml.lxml import parse
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

    try:
        xml_payload = StringIO(xml)
        tree = parse(xml_payload)
    except DefusedXmlException:
        return HttpResponse('Invalid XML input.', status=400)

    result = tree.xpath(f"/tag[@id={xpath}]")

    return HttpResponse(result)