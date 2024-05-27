from lxml import etree
from io import StringIO

from django.http import HttpResponse

def xpath_query(request):
    # Get the 'xpath' value from the GET request
    xpath = request.GET.get('xpath', '')

    # Get the 'xml' value from the GET request
    xml = request.GET.get('xml', '')

    # If 'xpath' or 'xml' is not defined, return an empty response
    if not xpath or not xml:
        return HttpResponse()

    # Construct and parse the xml payload
    parser = etree.XMLParser()
    try:
        tree = etree.parse(StringIO(xml), parser)
    except etree.ParseError:
        return HttpResponse()

    # Return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    result = tree.xpath("/tag[@id={}]".format(xpath))
    return HttpResponse(result)