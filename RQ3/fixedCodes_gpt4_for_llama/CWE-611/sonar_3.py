from lxml import etree


def transform_xml():
    parser = etree.XMLParser(recover=True,
                             no_network=True)  # Disable network access
    xslt_tree = etree.parse("resources/config.xsl", parser,
                            base_url="resources/")  # Set base URL for resolving relative paths
    xslt = etree.XSLT(xslt_tree)
    return xslt