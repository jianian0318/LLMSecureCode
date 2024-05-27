@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    # Get file name from request
    file_name = request.args.get('file_name')

    # Validate the request
    if file_name is None:
        return 'Invalid request. File name is missing.'

    # Check if the image file exists
    if not os.path.exists(file_name):
        return 'Error: Image file not found.'

    # Delete the image file
    os.remove(file_name)

    return 'Image file deleted successfully.'