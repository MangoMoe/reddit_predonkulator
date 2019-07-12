import praw
print('praw version: {}'.format(praw.__version__))
import uuid

import os
cwd = os.getcwd()
# print(cwd)

# User-agent preferred format: <platform>:<app ID>:<version string> (by /u/<reddit username>)
# do we need oauth? We aren't doing anything with users are we?
reddit = praw.Reddit(user_agent="web:Reddit Predonkulator:0.1 (by /u/MangoMo3)")

url = reddit.auth.url(['identity'], uuid.uuid4(), 'permanent')
# url = reddit.get_authorize_url('uniqueKey', 'identity', True)
import webbrowser
webbrowser.open(url)
# click allow on the displayed web page


# Example from the docs

# import praw
import pprint

# user_agent = ("Karma breakdown 1.0 by /u/_Daimon_ "
#               "github.com/Damgaard/Reddit-Bots/")
# r = praw.Reddit(user_agent=user_agent)
thing_limit = 10
user_name = "MangoMo3"
user = reddit.redditor(user_name)
print(user.id)
pprint.pprint(vars(user))
# gen = user.get_submitted(limit=thing_limit)
# karma_by_subreddit = {}
# for thing in gen:
#     subreddit = thing.subreddit.display_name
#     karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
#                                      + thing.score)
# pprint.pprint(karma_by_subreddit)