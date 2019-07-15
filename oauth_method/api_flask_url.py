from flask import abort, request, Flask
from flask_script import Manager, Server
from reddit_accessor import reddit_accessor
# this one below this line is incorrect, but the linter can't find the class unless its that way
# from oauth_method.reddit_accessor import reddit_accessor

app = Flask(__name__)
accessor = reddit_accessor()

def startup_accessor():
    print("Getting acessor ready")
    accessor.initial_authorization()

class CustomServer(Server):
    def __call__(self, app, *args, **kwargs):
        startup_accessor()
        #Hint: Here you could manipulate app
        return Server.__call__(self, app, *args, **kwargs)

manager = Manager(app)

# Remeber to add the command to your Manager instance
manager.add_command('runserver', CustomServer(port=9001))

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
    accessor.apply_authorization_code(code)
    return "got a code! %s" % code

if __name__ == '__main__':
    manager.run()
    # app.run(debug=True, port=9001)
    print("test?")