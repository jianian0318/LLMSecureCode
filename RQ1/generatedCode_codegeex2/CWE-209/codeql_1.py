from flask import Flask, Response
import traceback

app = Flask(__name__)


def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    '''
    在 try-except 块中调用 do_computation()，
    返回一个包含计算结果的 Response。
    '''
    try:
        result = do_computation()
        return Response(str(result))
    except Exception as e:
        traceback.print_exc()
        return Response(str(e), status=500)
