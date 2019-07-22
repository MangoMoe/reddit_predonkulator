import abc

class accessor_interface(abc.ABC):
    @abc.abstractmethod
    def get_subreddit(self):
        pass