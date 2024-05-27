from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    name = request.args.get('name')
    if name:                              # check if name parameter is not empty
       logging.info("Name: %s", name)     # Use parameterized logging to avoid crafted log entries 
       return "Logging successful"
    else:                                 # return error message if name parameter is empty
       return "No name parameter provided, logging unsuccessful"

if __name__ == '__main__':
    app.run()