from flask import Flask, request
import lxml.etree

app = Flask(__name__)


@app.post("/upload")
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    # 获取请求中的xml_src
    xml_src = request.form["xml_src"]
    # 解析xml_src
    root = lxml.etree.fromstring(xml_src)
    # 返回解析后的xml_src
    return lxml.etree.tostring(root, pretty_print=True).decode()

if __name__ == "__main__":
    app.run()
