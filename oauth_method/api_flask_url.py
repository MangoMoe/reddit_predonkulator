from flask import abort, request, Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<p>This is a homepage, trust me</p>"

@app.route('/authorize_callback')
def reddit_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    # state = request.args.get('state', '')
    code = request.args.get('code')
    # We'll change this next line in just a moment
    return "got a code! %s" % code

if __name__ == '__main__':
	app.run(debug=True, port=9001)