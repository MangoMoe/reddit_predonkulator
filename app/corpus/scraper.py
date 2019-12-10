import praw
import pprint
import time

reddit = praw.Reddit(user_agent="web:Reddit Predonkulator:0.1 (by /u/MangoMo3)")
subreddit_name = input("Please input subreddit name: ")
subreddit = reddit.subreddit(subreddit_name)

print("Subreddit name: {}\n".format(subreddit.display_name))

# print("Length of hot: {}\n".format(len(subreddit.hot())))
for submission in subreddit.hot(limit = 1):
    # top_level_comments = list(submission.comments)
    # all_comments = submission.comments.list()
    # submission = reddit.submission(id='39zje0')
    # submission.comment_sort = 'new'
    # top_level_comments = list(submission.comments)
    # print(submission.title)
    # pprint.pprint(vars(submission))
    print("Post text ---------------------------------------------------")
    print(submission.selftext)
    print("Comments ---------------------------------------------------")
    # This is important to fully flesh out the comment tree
    submission.comments.replace_more(0)
    top_level_comments = list(submission.comments)
    # all_comments = list(submission.comments)
    # this automatically does a breadth first search, but we want a depth first search
    # all_comments = submission.comments.list()
    # print(len(all_comments))
    # Using example code from https://praw.readthedocs.io/en/latest/tutorials/comments.html as a framework, also using CommentForrest documentation
    # also using various python documentation/tutorials (duh)
    # TODO to prepend the list just append (actually use extend) the other list to it duh
    #   TODO this might be significantly slower sincce we are replacing the list and rebuilding it each time but I'm not sure what else to do...
    # TODO make sure you use replace_more on the inner instances too
    comment_queue = top_level_comments[:]
    # TODO will replacing the comment queue affect the while loop?
    # TODO track depth with a separate queue that is the same length as comment_queue
    i = 0
    while comment_queue and i < 20:
        comment = comment_queue.pop(0)
        print("-------------------------------")
        print(comment.body)
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
        comment.replies.replace_more(0)
        temp_queue = comment.replies[:]
        temp_queue.extend(comment_queue)
        comment_queue = temp_queue
        i += 1

    # for comment in all_comments:
    #     # pprint.pprint(vars(comment))
    #     print(comment.body)
    #     # TODO you're probably gonna need some sort of recursive function
    #     for reply in comment.replies:
    #         print("reply")
    #     break
