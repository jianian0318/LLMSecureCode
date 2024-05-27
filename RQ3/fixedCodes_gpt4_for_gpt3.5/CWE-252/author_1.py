def parse(data):
    if data is None:
        return None
    return data.split(',')


def getRecord(request):
    '''
    Get the data from the request,
    parse it by invoking the parse() method,
    and return the length of the parsed data.
    '''
    data = request.get_data()
    if data is not None:
        parsed_data = parse(data)
        if parsed_data is not None:
            return len(parsed_data)
    return None