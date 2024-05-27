def parse(data):
    if data is None:
        return None
    return data.split(',')


def getRecord(request):
    '''
    从请求中获取数据，
    通过调用 parse() 方法解析它，
    并返回解析数据的长度。
    '''
    data = request.get_data(as_text=True)
    parsed_data = parse(data)
    if parsed_data is None:
        return 0
    return len(parsed_data)