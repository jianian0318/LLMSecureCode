from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    if request.method == 'POST':
        try:
            data = request.get_data()
            parsed_data = yaml.safe_load(data)
            return parsed_data
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run()