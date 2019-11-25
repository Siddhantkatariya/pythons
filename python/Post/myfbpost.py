class Post:
        title=None
        post=None


        def __init__(self, title, post):
            self.title=title
            self.post=post


        def get_post(self):
            return self.title +' '+ self.post

        def __str__(self):
            return self.title
