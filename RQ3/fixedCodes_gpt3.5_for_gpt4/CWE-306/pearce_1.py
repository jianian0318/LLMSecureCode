@app.route('/settings')
@ensure_logged_in
def settings():
    if current_user.is_authenticated:
        return '''<html>
        These are your confidential settings!
        </html>'''
    else:
        return "You must be logged in to access this page."