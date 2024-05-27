from bs4 import BeautifulSoup

def removeScriptTags(content):
    soup = BeautifulSoup(content, "html.parser")

    # Find and remove all script tags
    for script in soup(["script"]):
        script.extract()

    return str(soup)