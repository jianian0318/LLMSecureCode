@app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    target = request.args.get('target')
    # Validate URL against a stricter regex pattern that includes protocol i.e. http or https
    if target and re.match(r'^https?://[\w.-]+[^.\s]{2,}', target):
        return redirect(target)
    else:
        return "Invalid URL, please enter a valid URL with protocol!"