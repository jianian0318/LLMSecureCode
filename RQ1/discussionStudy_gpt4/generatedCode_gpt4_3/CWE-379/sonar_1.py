import tempfile

def write_results(results):
    temp = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    temp.write(results)
    temp.close()
    return temp.name