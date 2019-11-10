import praw
import string
from gtts import gTTS
from playsound import playsound
from praw.models import MoreComments


def get_link():
    reddit_link = input("Enter in a Reddit Post Link:")
    return reddit_link


def create_reddit_object():
    reddit = praw.Reddit(client_id='1rUc-2dGWkGqMw',
                         client_secret='az5cx5nCWFEqZeZ2Knlm4-oDYHI',
                         user_agent='OOF')

    return reddit


def get_data(link, reddit_object: praw.Reddit):
    submission = reddit_object.submission(url=link)
    title = submission.title
    body_text = submission.selftext
    author = submission.author.name
    return title, body_text, author

def master_string(title, body, author, comments):
    if body == '':
        body = 'Not Available'
    string = f"TITLE OF POST: {title}\nAUTHOR: {author}\nBODY: {body}\nTOP 5 COMMENTS: {comments}"
    return string


def say_post(text):
    return 0

def get_comments(link):
    aggregate_string = ''
    submission = create_reddit_object().submission(url=link)
    comments = submission.comments
    counter = 0
    for comment in comments:
        if isinstance(comment, MoreComments):
            continue
        aggregate_string += '\n\n'
        aggregate_string += 'Comment '
        aggregate_string += str(counter)
        aggregate_string += ': '
        aggregate_string += comment.body
        counter += 1
        if counter > 4:
            break
    return aggregate_string
