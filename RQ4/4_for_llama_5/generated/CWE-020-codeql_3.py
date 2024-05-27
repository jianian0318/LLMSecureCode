    target_url = request.args.get('target')
    if not target_url:
        return "No target URL provided", 400

    if not re.match(r'^https?://[^\s/$.?#].[^\s]*$', target_url):
        return "Invalid target URL", 400
    