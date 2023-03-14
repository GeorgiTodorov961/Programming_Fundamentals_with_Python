class Comment:

    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


# Part below is test code from example

comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)

