import pprint
import matplotlib.pyplot as plt

class analyzer:
    def __init__(self, accessor):
        self.accessor = accessor

    def analyze_subreddit(self, query):
        hot_posts = self.accessor.get_hot_posts(query,15)
        for post in hot_posts:

            # pprint.pprint(post.body_image)
            plt.imshow(post.body_image)
            break
        