import praw
import datetime
# For some reason relative imports above the current package fail unless we have this
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from app.accessor_interface import accessor_interface
from app.post_data import post_data
# TODO temp import
import pprint
import requests
import urllib, StringIO
from PIL import Image


# class oauth_accessor(accessor_interface.accessor_interface):
class oauth_accessor(accessor_interface):
    def __init__(self):
        self.reddit = None
        self.refresh_token = None
        self.refresh_time = datetime.datetime.now()

    def get_subreddit(self, subreddit_name):
       
        # print(self.reddit.subreddit(subreddit).submissions)
        
        return self.reddit.subreddit(subreddit_name)

    # TODO move to utility. can be used for json accessor as well
    def is_gif_url(self, url):
        if "gif" in url:
            return True
        elif "gfycat" in url:
            return True
        else:
            return False

    def get_hot_posts(self, subreddit_name, num_posts, images_only=True):   
        subreddit = self.get_subreddit(subreddit_name)
        # TODO break when we get enough of the right kind of post
        post_list = []
        for submission in subreddit.hot(limit=num_posts * 10):
            if images_only:
                # if the thumbnail height is not None and media is None and the url is not a gif, it is an image post
                if submission.thumbnail_height != None and submission.media == None and not self.is_gif_url(submission.url):
                    # img_data = requests.get(submission.url).content
                    file = cStringIO.StringIO(urllib.urlopen(submission.url).read())
                    img_data=Image.open(file)
                    width, height = img_data.size
                    print(width)
                    break
                    post_list.append(post_data(submission.title, img_data, None, submission.ups, submission.downs, None, None))
                    if len(post_list) >= num_posts:
                        break
            # TODO later figure out if text post
            # elif:
            #      pass
        return post_list

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
