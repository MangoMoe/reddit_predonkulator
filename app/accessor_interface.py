import abc

class accessor_interface(abc.ABC):
    @abc.abstractmethod
    def get_hot_posts(self, subreddit_name, num_posts, images_only=True):
        pass