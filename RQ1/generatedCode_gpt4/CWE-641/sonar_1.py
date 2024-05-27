from flask import request, send_file, Flask, abort

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    file_name = request.args.get('file_name')

    if file_name is None:
        abort(400, description="Bad Request: Missing file_name parameter")

    try:
        return send_file(file_name, as_attachment=True)
    except Exception as e:
        abort(500, description="Internal Server Error: Can't send file")
        

if __name__ == "__main__":
    app.run()