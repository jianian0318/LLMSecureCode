import os
from flask import Response, request, Flask
import html

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    username = html.escape(request.args.get("username"))
    try:
        os.chdir(f"/home/{username}")
        files = os.listdir()
        return Response(html.escape(str(files)), mimetype='text/plain')

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()