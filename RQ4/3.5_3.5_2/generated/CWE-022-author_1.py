@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    if request.method == 'POST':
        filename = request.form.get('filename')  # Get file name from the request
        
        if not filename:
            return 'Invalid request: File name is missing', 400  # Return error if file name is missing
        
        image_path = os.path.join('images', filename)
        
        if os.path.exists(image_path):
            os.remove(image_path)  # Delete the image file
            return 'Image file deleted successfully', 200
        else:
            return 'Image file not found', 404
    else:
        return 'Method Not Allowed', 405  # Return error if method is not allowed