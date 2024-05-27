from defusedxml.lxml import parse
from io import StringIO
from django.http import HttpResponse

def xpath_query(request):
    # Get the `xpath` value from the GET request
    xpath_value = request.GET.get('xpath')
    
    # Get the 'xml' value from the GET request
    xml_data = request.GET.get('xml')

    # Construct and parse the xml payload
    try:
        xml_payload = StringIO(xml_data)
        tree = parse(xml_payload)  # Use defusedxml's parse function
        
        # Return the result of the XPath query "/tag[@id={}]" format from the parsed xml
        query = f"/tag[@id='{xpath_value}']"
        results = tree.xpath(query)

        # Process results and construct HttpResponse
        if results:
            result_string = "".join([etree.tostring(result).decode('utf-8') for result in results])
            return HttpResponse(result_string, content_type="application/xml")
        else:
            return HttpResponse("No matching elements found.", status=404)
    except etree.XMLSyntaxError:
        return HttpResponse("Error processing XML data.", status=400)
    except Exception:
        # Do not provide the exception message or stack trace to the end user.
        return HttpResponse("Internal server error.", status=500)