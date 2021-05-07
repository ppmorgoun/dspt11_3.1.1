from mymodule.reddit import User, Comment

ryan = User(name='ryan', karma='5000', is_moderator=False)
susan = User(name='Susan', karma='3000', is_moderator=False)
windsurfing_topic = ryan.post_topic(title='windsurfing is cool', body='...')
troll_comment = ryan.post_comment(
    topic=windsurfing_topic,
    body='windsurfing sux dix')
nice_comment = Comment(
    topic=windsurfing_topic,
    body='<3',
    down_votes=0,
    up_votes=10000,
    user=ryan)

print(nice_comment.up_votes)

ryan.up_vote(nice_comment)
go_windsurfing_comment = susan.post_comment(
    topic=windsurfing_topic,
    body="wanna go surfing with me?")
ryan.up_vote(go_windsurfing_comment)

print(go_windsurfing_comment.up_votes)
print([i.title for i in ryan.topics], [i.body for i in susan.comments])
