from lxml import etree

def getXmlRoot():
    '''
    Create an XML parser and parse the resources/c.xml file and return the root element
    '''
    # 解析 resources/c.xml 文件
    xml_tree = etree.parse('resources/c.xml')
    # 获取根元素
    root = xml_tree.getroot()
    return root
