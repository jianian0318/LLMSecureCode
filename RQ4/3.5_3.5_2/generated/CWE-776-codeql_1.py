    if 'file' not in request.files:
        return "No file part in the request", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.xml'):
        xml_data = file.read()
        root = ET.fromstring(xml_data)
        return ET.tostring(root), 200
    else:
        return "Uploaded file is not XML", 400