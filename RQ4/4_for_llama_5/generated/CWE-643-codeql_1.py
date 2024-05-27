    def xpath_query(request):
        xpath = request.GET.get('xpath')
        xml = request.GET.get('xml')

        if not xpath or not xml:
            return HttpResponse("Missing required parameters", status=400)

        try:
            xml_tree = etree.parse(StringIO(xml))
            result = xml_tree.xpath(xpath)
        except Exception as e:
            return HttpResponse(f"Error processing request: {e}", status=400)

        return HttpResponse(str(result), status=200)
    