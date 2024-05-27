import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    clean_content = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', content, flags=re.DOTALL)
    return clean_content