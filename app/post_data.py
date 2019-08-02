class post_data:
    def __init__(self, title, body_image, body_text, upvotes, downvotes, number_of_comments, flair):
        # TODO finish this method
        # Top, new, rising, controversial, Hot
        # Duration
                
        # can't have both text and image
        # either have image and maybe description in comment or have text with link to an image
            
        self.title = title
        self.body_image = body_image
        self.body_text = body_text
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.number_of_comments = number_of_comments
        self.flair = flair