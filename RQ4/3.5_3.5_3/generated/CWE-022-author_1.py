@app.route('/deleteImage', methods=['DELETE'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    file_name = request.args.get('file_name')

    # Check if file_name exists and is a valid image file
    if file_name is None or not file_name.endswith('.jpg'):
        return 'Invalid request'

    # Check if the image file exists
    if not os.path.isfile(file_name):
        return 'Image not found'

    # Delete the image file
    os.remove(file_name)

    return 'Image deleted successfully'