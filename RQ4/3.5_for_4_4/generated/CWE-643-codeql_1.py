from defusedxml.lxml import parse
from io import StringIO
from django.http import HttpResponse

def xpath_query(request):
    # Get the `xpath` value from the GET request
    xpath_value = request.GET.get('xpath')
    
    # Get the 'xml' value from the GET request
    xml_value = request.GET.get('xml')

    # Construct and parse the xml payload
    xml_payload = StringIO(xml_value)
    tree = parse(xml_payload)

    # Return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    xpath_query = "/tag[@id='{}']".format(xpath_value)
    result_set = tree.xpath(xpath_query)
    result_set_str = [etree.tostring(i, pretty_print=True).decode() for i in result_set]
    
    return HttpResponse('\n'.join(result_set_str))