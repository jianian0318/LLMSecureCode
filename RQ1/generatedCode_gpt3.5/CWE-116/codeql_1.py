import re


def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    content = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', content)
    return content