import re


def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    content = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', content)
    content = re.sub(r'&lt;script\b[^<]*(?:(?!&lt;\/script>)<[^<]*)*&lt;\/script&gt;', '', content)
    return content