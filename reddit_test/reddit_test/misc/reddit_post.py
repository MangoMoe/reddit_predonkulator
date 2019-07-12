
class reddit_post:
    # Get title, body text, image, links, num upvotes
    def __init__(self, title, body, img, links, upvotes):
        self.title = title
        self.body = body
        self.img = img
        self.links = links
        self.upvotes = upvotes