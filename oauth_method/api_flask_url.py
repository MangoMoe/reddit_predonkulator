from flask import abort, request, Flask
from reddit_accessor import reddit_accessor
# this one below this line is incorrect, but the linter can't find the class unless its that way
# from oauth_method.reddit_accessor import reddit_accessor

app = Flask(__name__)

class web_endpoint:
    def __init__(self):
        global app
        self.app = app
        self.accessor = reddit_accessor()
        # TODO should we run this here or only after a multithreaded server is running for sure?
        self.accessor.initial_authorization()

# TODO these can't have self in them, they are callbacks, so we will have to put them outside of a class
    @app.route('/')
    def homepage(self):
        return "<p>This is a homepage, trust me</p>"

    @app.route('/authorize_callback')
    def reddit_callback(self):
        error = request.args.get('error', '')
        if error:
            return "Error: " + error
        # state = request.args.get('state', '')
        code = request.args.get('code')
        self.accessor.apply_authorization_code(code)
        # We'll change this next line in just a moment
        # return "got a code! %s" % code
        return

if __name__ == '__main__':
    endpoint = web_endpoint()
    # TODO make this multithreaded?
    endpoint.app.run(debug=True, port=9001)
    print("test?")