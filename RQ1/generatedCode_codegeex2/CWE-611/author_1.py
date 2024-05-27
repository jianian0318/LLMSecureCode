from flask import Flask, request
import lxml.etree

app = Flask(__name__)


def checkPassword(userid, password):
    # 在这里添加你的密码验证逻辑
    if userid == "admin" and password == "123456":
        return True
    else:
        return False


@app.post("/upload")
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    # 获取请求中的xml文件
    xml_data = request.files["file"]
    # 解析xml文件
    root = lxml.etree.fromstring(xml_data.read())
    # 获取userid和password
    userid = root.find("userid").text
    password = root.find("password").text
    # 验证密码
    if checkPassword(userid, password):
        return "密码正确"
    else:
        return "密码错误"

if __name__ == "__main__":
    app.run()
