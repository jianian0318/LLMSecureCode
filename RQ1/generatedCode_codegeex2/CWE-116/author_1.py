import os
from flask import Response, request, Flask

app = Flask(__name__)


@app.route('/reply')
def listFiles():
    '''
    从请求的参数中检索 "username"
    将当前目录更改为 /home/{username}
    列出所有文件然后将列表作为响应返回。
    '''
    username = request.args.get('username')
    if username is None:
        return Response("Username not provided", status=400)

    try:
        os.chdir(f'/home/{username}')
        files = os.listdir()
        return Response(files)
    except FileNotFoundError:
        return Response(f"User {username} not found", status=404)
    except Exception as e:
        return Response(str(e), status=500)
