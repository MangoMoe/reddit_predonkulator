import abc

class accessor_interface(abc.ABC):
    @abc.abstractmethod
    def get_subreddit(self, subreddit_name):
        pass

    @abc.abstractmethod
    def get_hot_posts(self, subreddit_name, duration, num_posts):
        # TODO make enum for duration
        pass