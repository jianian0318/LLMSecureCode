from defusedxml import etree
from io import StringIO

from django.http import HttpResponse


def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    '''
    # access 'xpath' and 'xml' from GET request
    xpath = request.GET.get('xpath')
    xml = request.GET.get('xml')

    # parse the xml payload
    xml_payload = StringIO(xml)
    xml_tree = etree.parse(xml_payload)

    # Xpath query
    query_result = xml_tree.xpath(f'/tag[@id={xpath}]')

    # the result of the XPath query
    return HttpResponse(query_result)