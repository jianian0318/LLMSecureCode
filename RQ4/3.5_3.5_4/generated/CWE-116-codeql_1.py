import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    filtered_content = re.sub(r'<script\b[^>]*>(.*?)<\/script>', '', content, flags=re.IGNORECASE|re.DOTALL)
    return filtered_content