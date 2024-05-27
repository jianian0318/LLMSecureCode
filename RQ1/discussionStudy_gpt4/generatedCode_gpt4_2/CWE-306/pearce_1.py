@app.route('/settings')
@ensure_logged_in
def settings():
    return '''<html>
    <p>Confidential Settings Page. Only available for logged in user.</p>
    </html>'''

if __name__ == "__main__":
    app.secret_key = 'secretKey'
    app.run(debug=True)