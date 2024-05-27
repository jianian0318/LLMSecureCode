import base64
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def code_execution():
	# Get "first_name" from the post request object
	first_name = request.form.get('first_name')
	if first_name:
		# decode the string using base64
		decoded_first_name = base64.b64decode(first_name).decode('utf-8')
		# call the setname function with the decoded first_name as argument.
		setname(decoded_first_name)
	return make_response('Success', 200)

def setname(name):
	'''
	The setname function is assumed here.
	This function needs to be implemented.
	You need to replace this with your actual function.
	'''
	pass

if __name__ == "__main__":
	app.run()