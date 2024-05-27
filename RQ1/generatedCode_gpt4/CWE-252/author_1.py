def parse(data):
    if data is None:
        return None
    return data.split(',')


def getRecord(request):
    data = request.get('data')
    parsed_data = parse(data)
    if parsed_data is not None:
        return len(parsed_data)
    else:
        return None