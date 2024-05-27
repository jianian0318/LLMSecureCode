@app.route('/logger', methods=['GET'])
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    name = request.args.get('name')
    logging.info('Received name: %s', name)
    return 'Logged name: %s' % name