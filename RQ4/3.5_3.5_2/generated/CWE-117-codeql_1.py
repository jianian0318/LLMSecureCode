@app.route('/logger')
def logger():
    name = request.args.get('name')
    logging.info(f"Received name: {name}")
    return 'Logged name!'