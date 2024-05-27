from defusedxml.lxml import etree
from io import StringIO

from django.http import HttpResponse


def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    '''
    xpath_value = request.GET.get('xpath')    # get xpath from GET request
    xml_value = request.GET.get('xml')        # get xml content from GET request

    # Parse the XML document and turn it into an lxml ElementTree object using defusedxml library.
    tree = etree.parse(StringIO(xml_value))

    # Prepare the XPath query
    xpath_query_string = f"/tag[@id='{xpath_value}']"

    # Perform the XPath query.
    result = tree.xpath(xpath_query_string)

    # Return the xpath query result
    return HttpResponse(result)