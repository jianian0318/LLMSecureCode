from flask import request, Response, Flask, redirect

app = Flask(__name__)


@app.route('/set_location_header')
def set_location_header():
    next_url = request.args.get('next')
    return redirect(next_url)


if __name__ == "__main__":
    app.run(debug=True)