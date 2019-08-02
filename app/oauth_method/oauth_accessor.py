import praw
import datetime
# For some reason relative imports above the current package fail unless we have this
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from app.accessor_interface import accessor_interface

# class oauth_accessor(accessor_interface.accessor_interface):
class oauth_accessor(accessor_interface):
    def __init__(self):
        self.reddit = None
        self.refresh_token = None
        self.refresh_time = datetime.datetime.now()

    def get_subreddit(self, subreddit_name):
        print("Name: ", self.reddit.subreddit(subreddit_name).display_name)
        print("Subreddit stuff: ", self.reddit.subreddit(subreddit_name))
        print(self.reddit.user.me())
        print(self.reddit.auth.scopes())
        # print(self.reddit.subreddit(subreddit).submissions)
        for submission in self.reddit.subreddit(subreddit_name).hot():
            print(submission.title)
        return self.reddit.subreddit(subreddit_name)

    def reauthorize(self):
        self.refresh_with_token()
        
    def is_authorized(self):
        if self.reddit == None:
            return False
        elif self.refresh_time <= datetime.datetime.now()-datetime.timedelta(minutes=60):
            return False
        else:
            return True

    def can_refresh(self):
        return self.refresh_token != None
    
    def initial_authorization(self):
        # User-agent preferred format: <platform>:<app ID>:<version string> (by /u/<reddit username>)
        self.reddit = praw.Reddit(user_agent="web:Reddit Predonkulator:0.1 (by /u/MangoMo3)")

        import uuid
        url = self.reddit.auth.url(['identity', 'read'], uuid.uuid4(), 'permanent')
        print("Initial authorization url found")
        return url

    def apply_authorization_code(self, code):
        # this line shows the logged in user and lets us know it worked correctly and we are authorized
        print(self.reddit.user.me())
        self.refresh_token = self.reddit.auth.authorize(code)
        print(self.refresh_token)
        print(self.reddit.user.me())
        print(self.reddit.auth.scopes())
        print("Authorization code applied, we should be authorized now")

    def refresh_with_token(self):
        self.reddit = praw.Reddit(refresh_token=self.refresh_token,
                                    user_agent="web:Reddit Predonkulator:0.1 (by /u/MangoMo3)")
        self.refresh_time = datetime.datetime.now()
