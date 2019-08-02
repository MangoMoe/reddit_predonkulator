from flask import abort, request, redirect, Flask, render_template
from flask_script import Manager, Server
from oauth_method.oauth_accessor import oauth_accessor

from reddit_analyzer.analyzer import analyzer as red_analyzer
# this one below this line is incorrect, but the linter can't find the class unless its that way
# from oauth_method.reddit_accessor import reddit_accessor


app = Flask(__name__)
app.config['DEBUG'] = True
accessor = oauth_accessor()
analyser=None
def startup_accessor():
    print("Getting acessor ready")
    return accessor.initial_authorization()

class CustomServer(Server):
    def __call__(self, app, *args, **kwargs):
        #Hint: Here you could manipulate app
        return Server.__call__(self, app, *args, **kwargs)


manager = Manager(app)

# Remeber to add the command to your Manager instance
manager.add_command('runserver', CustomServer(port=9001))
redirect_url = "localhost:9001"

def authorize(uri):
    global redirect_url
    redirect_url = uri
    if accessor.can_refresh():
        accessor.reauthorize()
    else:
        # get authorized through url and get refresh token
        url = startup_accessor()
        return redirect(url, code=202)
    return None

@app.route('/')
def homepage():
    needs_authorization = authorize("/")
    if needs_authorization != None:
        return needs_authorization
    return render_template("homepage.html")

@app.route('/predonkulator')
def predonkulator_page():
    query = request.args.get('subreddit')
    uri = "/predonkulator"
    if query != None:
        uri+="?subreddit="+query
    needs_authorization = authorize(uri)
    if needs_authorization != None:
        return needs_authorization

    if query != None:
        print(query)
        # TODO put this somewhere else, in another package
        analyzer = red_analyzer(accessor)
        analyzer.analyze_subreddit(query)

    return render_template("predonkulator.html")

@app.route('/authorize_callback')
def reddit_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    # state = request.args.get('state', '')
    code = request.args.get('code')
    accessor.apply_authorization_code(code)
    # return render_template("homepage.html")
    return redirect(redirect_url)

if __name__ == '__main__':
    manager.run()
    # app.run(debug=True, port=9001)
    print("test?")