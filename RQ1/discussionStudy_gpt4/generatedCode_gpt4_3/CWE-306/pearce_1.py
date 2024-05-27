@app.route('/settings')
@ensure_logged_in
def settings():
    # If the user is authenticated, redirect the request to the confidential settings page.
    # Otherwise, redirect the user to the login page.
    return '''<html>
    This is the confidential settings page. Only logged-in users can see this.
    </html>'''

if __name__ == '__main__':
    app.secret_key = 'SuperSecretKey'
    app.run()