import praw
import pprint
import time

reddit = praw.Reddit(user_agent="web:Reddit Predonkulator:0.1 (by /u/MangoMo3)")
subreddit_name = input("Please input subreddit name: ")
subreddit = reddit.subreddit(subreddit_name)

print("Subreddit name: {}\n".format(subreddit.display_name))

# print("Length of hot: {}\n".format(len(subreddit.hot())))
for submission in subreddit.hot(limit = 1):
    # print(submission.title)
    # pprint.pprint(vars(submission))
    print("Post text ---------------------------------------------------")
    print(submission.selftext)
    print("Comments ---------------------------------------------------")
    # This is important to fully flesh out the comment tree
    # submission.refresh()
    submission.comments.replace_more(0)
    top_level_comments = list(submission.comments)
    # this automatically does a breadth first search, but we want a depth first search
    #   all_comments = submission.comments.list()
    # Using example code from https://praw.readthedocs.io/en/latest/tutorials/comments.html as a framework, also using CommentForrest documentation
    #   also using various python documentation/tutorials (duh)
    comment_queue = top_level_comments[::-1]
    indentation_levels = [0]*len(comment_queue)
    # print(indentation_levels)
    # TODO track depth with a separate queue that is the same length as comment_queue
    i = 0
    while comment_queue and i < 20:
        # print("-------------------------------")
        comment = comment_queue.pop()
        indentation_level = indentation_levels.pop()
        indentation = "\t" * indentation_level
        print(indentation + comment.body)
        # TODO see the praw documentation for CommentForrest to figure out how to do this safely in a loop
        #   trying this out below
        # while True:
        #     try:
        #         # replies is also a CommentForrest object so this should work
        #         comment.replies.replace_more(0)
        #         break
        #     except Exception as e:
        #         print('Handling replace_more exception')
        #         print("exception was: \n{}".format(str(e)))
        #         time.sleep(1)
        # print("*******")
        # print(len(list(comment.replies)))
        comment.refresh() # for some reason this refresh is vital or else it doesn't get all the comments
        comment.replies.replace_more(0)
        # print(len(list(comment.replies)))
        comment_queue.extend(list(comment.replies[::-1]))
        indentation_levels.extend([indentation_level + 1] * len(list(comment.replies)))
        i += 1