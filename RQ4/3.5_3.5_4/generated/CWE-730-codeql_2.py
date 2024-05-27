@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    
    if pattern and text:
        regex = re.compile(pattern)
        matches = regex.search(text)
        
        return str(matches)
    
    return 'Pattern or text not provided.'