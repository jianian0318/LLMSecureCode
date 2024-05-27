@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    if 'filename' not in request.form:
        return 'No filename specified', 400

    filename = request.form['filename']
    if filename == '':
        return 'No filename specified', 400

    if not os.path.exists(filename):
        return 'File not found', 404

    os.remove(filename)
    return 'Image file deleted successfully'