import os
from flask import Response, request, Flask
import html

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    username = request.args.get("username")
    try:
        os.chdir(f"/home/{username}")
        files = os.listdir()
        files_str = "\n".join(files)
        return Response(html.escape(files_str), mimetype='text/plain')

    except Exception as e:
        return html.escape(str(e))

if __name__ == '__main__':
    app.run()