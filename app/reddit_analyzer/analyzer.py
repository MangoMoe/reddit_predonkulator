class analyzer:
    def __init__(self, accessor):
        self.accessor = accessor

    def analyze_subreddit(self, query):
        subreddit = self.accessor.get_subreddit(query)
        
        