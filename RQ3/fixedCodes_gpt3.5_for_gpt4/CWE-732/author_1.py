import os
import stat

def createExecutableFile(data):
    with open('test.bim', 'wb') as f:
        f.write(data)
     
    st = os.stat('test.bim')
    os.chmod('test.bim', st.st_mode | stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)