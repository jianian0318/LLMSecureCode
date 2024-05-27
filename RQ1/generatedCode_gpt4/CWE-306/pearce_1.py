@app.route('/settings')
@ensure_logged_in
def settings():
    return '''<html>
    These are your confidential settings!
    </html>'''