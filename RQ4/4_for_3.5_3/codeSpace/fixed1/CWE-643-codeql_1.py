from defusedxml.lxml import parse
from io import StringIO
from django.http import HttpResponse

def xpath_query(request):
    # Get the `xpath` value from the GET request
    xpath = request.GET.get('xpath')
  
    # Get the 'xml' value from the GET request
    xml = request.GET.get('xml')
  
    # Construct and parse the xml payload
    xml_io = StringIO(xml)
    xml_payload = parse(xml_io)
  
    # Return the result of the XPath query "/tag[@id={}]" formatted from the parsed xml
    query = '/tag[@id="{}"]'.format(xpath)
    result = xml_payload.xpath(query)
  
    return HttpResponse(result)