@app.route('/log', methods=['GET'])
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    input = request.args.get('input')
    current_app.logger.error(input)
    return "Logged as error"