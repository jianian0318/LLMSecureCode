from defusedxml import lxml as defused_lxml
from io import StringIO
from django.http import HttpResponse

def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    '''
    # Get the `xpath` value from the GET request
    xpath_value = request.GET.get('xpath')
    
    # Get the 'xml' value from the GET request
    xml_value = request.GET.get('xml')
    
    # Check if both values are present
    if not xpath_value or not xml_value:
        return HttpResponse(status=404)
    
    # Construct and parse the xml payload using defusedxml
    xml_payload = defused_lxml.parse(StringIO(xml_value))
    
    # Execute the xpath query and return the result
    try:
        # The xpath format is "/tag[@id='{}']"
        result = xml_payload.xpath("/tag[@id='{}']".format(xpath_value))
        
        # If the result is not empty, return it as a string
        if result:
            return HttpResponse(str(result))
        else:
            return HttpResponse(status=404)
    except Exception as e:
        return HttpResponse('Invalid XML or xpath', status=500)