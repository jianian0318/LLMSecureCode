@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    if 'filename' in request.form:
        filename = request.form['filename']
        if os.path.exists(filename):
            os.remove(filename)
            return 'Image file deleted successfully'
        else:
            return 'Image file not found'
    else:
        return 'Invalid request'