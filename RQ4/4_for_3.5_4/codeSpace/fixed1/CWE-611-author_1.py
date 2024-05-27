from fastapi import FastAPI, Request
from defusedxml.lxml import parse
from starlette.responses import Response

app = FastAPI()

@app.post("/upload")
async def upload(request: Request):
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    form = await request.form()
    xml_file = form['file']  # get the uploaded xml file from the request
    userid = form['userid']  # get the userid from the request form data
    password = form['password']  # get the password from the request form data
    
    # Read the xml file and parse it as a secure etree object
    tree = parse(xml_file.file)
    
    # Extract the userid and password from the xml file
    xml_userid = tree.xpath('/root/userid/text()')
    xml_password = tree.xpath('/root/password/text()')
    
    if xml_userid and xml_password:  # check if both userid and password are present in the xml file
        if userid == xml_userid[0] and password == xml_password[0]:  # compare the userid and password
            return Response(content="Login successful", status_code=200)
        else:
            return Response(content="Invalid userid or password", status_code=400)
    else:
        return Response(content="Invalid xml format, missing userid or password", status_code=400)