import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage', methods=['POST']) #change method to POST
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    file_name = request.form.get('file_name') #get file_name from form data

    if not file_name: #validate if file_name exist
        return "Bad Request", 400

    try:
        os.remove(file_name) #delete the file
        return "Success", 200
    except FileNotFoundError:
        return "File not found", 404
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)