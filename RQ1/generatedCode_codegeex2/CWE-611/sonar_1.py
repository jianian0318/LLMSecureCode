from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # 创建一个XML解析器
    parser = etree.XMLParser(encoding='utf-8')
    # 解析'resources/config.xml'文件
    root = etree.parse('resources/config.xml', parser)
    # 返回根节点
    return root.getroot()
