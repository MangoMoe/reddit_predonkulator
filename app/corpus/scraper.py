import praw
import pprint
from tqdm import tqdm
import numpy as np

reddit = praw.Reddit(user_agent="web:Reddit Predonkulator:0.1 (by /u/MangoMo3)")
subreddit_name = input("Please input subreddit name: ")
subreddit = reddit.subreddit(subreddit_name)

print("Subreddit name: {}\n".format(subreddit.display_name))

with open(subreddit_name + "_corpus_file.corp", "w", encoding="utf-8") as corpus_file:
    i = 0
    queue_lengths = []
    for submission in tqdm(subreddit.hot(limit = 1)):
        i += 1
        corpus_file.write("\"" + submission.selftext + "\"")
        # This is important to fully flesh out the comment tree
        submission.comments.replace_more(limit=None)
        top_level_comments = list(submission.comments)
        # this automatically does a breadth first search, but we want a depth first search
        #   all_comments = submission.comments.list()
        # Using example code from https://praw.readthedocs.io/en/latest/tutorials/comments.html as a framework, also using CommentForrest documentation
        #   also using various python documentation/tutorials (duh)
        # if you have errors with MoreComments objects, see the praw documentation for CommentForrest to figure out how to do this safely in a loop
        comment_queue = top_level_comments[::-1]
        indentation_levels = [1]*len(comment_queue)
        queue_length = len(comment_queue)
        while comment_queue:
            comment = comment_queue.pop()
            indentation_level = indentation_levels.pop()
            indentation = "\t" * indentation_level
            comment_body = "\r\n\"" + comment.body + "\""
            # found on stack overflow
            corpus_file.write(indentation.join(comment_body.splitlines(True))[1:])
            # This slows things down incrementally, while using limit=None above in submission.comments.replace_more slows it down all at once, I'm not really sure if there is a difference
            # comment.refresh() # for some reason this refresh is vital or else it doesn't get all the comments
            comment.replies.replace_more(limit=None)
            queue_length += len(list(comment.replies))
            comment_queue.extend(list(comment.replies[::-1]))
            indentation_levels.extend([indentation_level + 1] * len(list(comment.replies)))
        queue_lengths.append(queue_length)
    print("Average number of comments per post was: {}".format(np.mean(np.array(queue_lengths))))