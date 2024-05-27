from defusedxml.lxml import parse
from io import StringIO

from django.http import HttpResponse

def xpath_query(request):
    # Get the 'xpath' value from the GET request
    xpath_value = request.GET.get('xpath')

    # Get the 'xml' value from the GET request
    xml_value = request.GET.get('xml')

    # Construct and parse the xml payload using defusedxml
    xml_payload = parse(StringIO(xml_value))

    # Return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    result = xml_payload.xpath("/tag[@id={}]".format(xpath_value))
    result_str = ','.join([str(item) for item in result])

    return HttpResponse(result_str)