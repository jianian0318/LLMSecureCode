from lxml import etree
from io import StringIO

from django.http import HttpResponse


def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    '''

    # Get the `xpath` value from the GET request parameters
    xpath = request.GET.get('xpath')

    # Get the `xml` value from the GET request parameters
    xml = request.GET.get('xml')

    # Construct and parse the xml payload
    parser = etree.XMLParser()
    root = etree.parse(StringIO(xml), parser)

    # Return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    result = root.xpath("/tag[@id='{}']".format(xpath))
    return HttpResponse(result)