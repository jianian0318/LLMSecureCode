@app.route("/profile")
def profile():
    raw_data = request.get_data(as_text=True)  # get raw data from request as text
    decoded_data = base64.b64decode(raw_data)  # decode the base64 encoded data
    data = pickle.loads(decoded_data)  # deserialize the decoded data
    return data  # return the deserialized data