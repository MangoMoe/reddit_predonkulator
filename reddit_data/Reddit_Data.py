import Reddit_Post

class Reddit_Data:
    def _init_(self,posts,after):
        self.post = self.getPosts(posts)
        self.after = after

    @staticmethod
    def getPosts(posts):
        post_list = []
        for post in posts:
            post_list.append(Reddit_Post.fromJson(post))

        return post_list