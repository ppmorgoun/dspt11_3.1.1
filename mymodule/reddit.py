admin = "petr"


class Post:
    def __init__(self, up_votes, down_votes, user, body):
        self.up_votes = up_votes
        self.down_votes = down_votes
        self.user = user
        self.body = body


class User:
    def __init__(self, name, karma, is_moderator=False):
        """
            Create a User object
            ------------
            name : str
            Returns
        """
        self.name = name
        self.karma = karma
        self.is_moderator = is_moderator
        self.topics = []
        self.comments = []
        print(f'New user created:\nName = {self.name}\nKarma = {self.karma}')

    def post_topic(self, title, body):
        """
            Post a topic with the user as the author and the given title and body
            ------------
            title : str
            Returns
            --------
            Topic
        """
        topic = Topic(title=title, user=self, body=body)
        self.topics.append(topic)
        return topic

    def post_comment(self, topic, body):
        comment = Comment(topic=topic, body=body, user=self)
        self.comments.append(comment)
        return comment

    """
    Argument post is expected to be either a mymodule.reddit.Topic object or mymodule.reddit.Comment
    """

    def up_vote(self, post: Post):
        post.up_votes += 1


class Topic(Post):
    def __init__(self, title, user, body, up_votes=1, down_votes=0):
        self.title = title
        super(Topic, self).__init__(up_votes=up_votes, down_votes=down_votes, user=user, body=body)


class Comment(Post):
    def __init__(self, topic, body, user, up_votes=1, down_votes=0):
        self.topic = topic
        super(Comment, self).__init__(up_votes=up_votes, down_votes=down_votes, user=user, body=body)
