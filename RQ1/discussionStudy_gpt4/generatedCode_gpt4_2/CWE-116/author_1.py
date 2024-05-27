import os
from flask import Response, request, Flask

app = Flask(__name__)


@app.route('/reply')
def listFiles():
    username = request.args.get("username")
    os.chdir(f"/home/{username}")
    files = os.listdir()
    return Response(str(files), mimetype='text/plain')


if __name__ == "__main__":
    app.run()