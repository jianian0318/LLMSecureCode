@app.route('/logger', methods=['GET'])    # Specify the allowed request method
def logger():
    name = request.args.get('name')    # Get the "name" value from the GET request
    logging.info(name)    # Log the name as an information message
    return "Logged: {}".format(name)    # Return a response acknowledging the logging