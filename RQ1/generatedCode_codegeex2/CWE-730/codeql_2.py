from flask import request
import re


@app.route("/direct")
def direct():
    '''
    从GET请求中获取正则表达式模式（pattern），编译它
    并在GET请求中的'text'字符串中使用它进行搜索。
    '''
    pattern = request.args.get("pattern", "")
    text = request.args.get("text", "")

    if not pattern or not text:
        return "Error: Missing pattern or text parameter"

    try:
        re.compile(pattern)
    except re.error:
        return "Error: Invalid regular expression pattern"

    matches = re.search(pattern, text)
    if matches:
        return "Matched: " + str(matches.group(0))
    else:
        return "No match found"