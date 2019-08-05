from PIL import Image
class post_data:
    def __init__(self, title, body_image, body_text, upvotes, downvotes, number_of_comments, flair):
        # can't have both text and image
        # either have image and maybe description in comment or have text with link to an image
            
        self.title = title

        # TODO this convert png to rgb format, use it
        # print(type(body_image))
        self.body_image = Image.frombytes('RGBA', (int(len(body_image)**.5),int(len(body_image)**.5)), body_image, 'raw')
        # rgb_im.save('colors.jpg')

        # self.body_image = body_image
        self.body_text = body_text
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.number_of_comments = number_of_comments
        self.flair = flair

# To save an image
# with open('image_name.jpg', 'wb') as handler:
#     handler.write(img_data)