@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    # Get file name from request
    file_name = request.form.get('file_name')

    # Check if the file name is provided
    if file_name is None:
        return 'File name is required', 400

    # Check if the file exists
    if not os.path.exists(file_name):
        return 'File not found', 404

    # Delete the image file
    os.remove(file_name)

    return 'Image file deleted successfully', 200