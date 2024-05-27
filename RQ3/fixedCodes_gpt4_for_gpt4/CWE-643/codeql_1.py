from lxml import etree
from io import StringIO

from django.http import HttpResponse


def xpath_query(request):
    # Get the `xpath` value from the GET request
    xpath_value = request.GET.get('xpath')

    # Get the 'xml' value from the GET request
    xml_value = request.GET.get('xml')

    # Construct and parse the xml payload
    xml_parser = etree.XMLParser(ns_clean=True)
    xml_payload = etree.parse(StringIO(xml_value), xml_parser)

    # Return the result of the XPath query using safe method to prevent injection
    xpath_result = xml_payload.xpath("/tag[@id=$id]", id=xpath_value)
    
    # Format result to string for HttpResponse
    result_string = '\n'.join([etree.tostring(elem).decode('utf-8') for elem in xpath_result])
    
    return HttpResponse(result_string)