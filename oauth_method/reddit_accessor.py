import praw

class reddit_accessor:
    def __init__(self):
        self.reddit = None
        self.refresh_token = None
    
    def initial_authorization(self):
        # User-agent preferred format: <platform>:<app ID>:<version string> (by /u/<reddit username>)
        self.reddit = praw.Reddit(user_agent="web:Reddit Predonkulator:0.1 (by /u/MangoMo3)")

        import uuid
        url = self.reddit.auth.url(['identity'], uuid.uuid4(), 'permanent')
        import webbrowser
        # click allow on the displayed web page
        webbrowser.open(url)

    def apply_authorization_code(self, code):
        # this line shows the logged in user and lets us know it worked correctly and we are authorized
        print(self.reddit.user.me())
        self.refresh_token = self.reddit.auth.authorize(code)
        print(self.refresh_token)
        print(self.reddit.user.me())
        print(self.reddit.auth.scopes())

    def refresh_with_token(self):
        self.reddit = praw.Reddit(refresh_token=self.refresh_token,
                     user_agent="web:Reddit Predonkulator:0.1 (by /u/MangoMo3)")