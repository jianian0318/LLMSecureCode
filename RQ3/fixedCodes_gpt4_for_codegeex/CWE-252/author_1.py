def parse(data):
    if data is None:
        return None
    return data.split(',')


def getRecord(request):
    '''
    Retrieves data from the request,
    parses it by calling the parse() method,
    and returns the length of the parsed data.
    '''
    data = request.get_data(as_text=True)
    parsed_data = parse(data)
    if parsed_data is None:
        return "Parsing unsuccessful. No data to return."
    return len(parsed_data)