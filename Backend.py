# Back end functionality for Readit application.
# Readit will prompt the user for a link to a reddit post, then use text to speech software to
# read the reddit post and the top 5 comments aloud to the user
# Uses gtts, playsound and praw external libraries. Must install using pip install (or python -m pip install)
# Authors: Josh Duran, Kenny Ngo, Alex Debont, Chase Pan
# Created for HackUTD 2019

import praw
import string
from gtts import gTTS
from playsound import playsound
from praw.models import MoreComments


# Creates and initializes reddit object
def create_reddit_object():
    reddit = praw.Reddit(client_id='1rUc-2dGWkGqMw',
                         client_secret='az5cx5nCWFEqZeZ2Knlm4-oDYHI',
                         user_agent='OOF')

    return reddit


# Gets reddit link and reddit object as input
# Outputs ie returns the title, body text and author of the reddit post
def get_data(link, reddit_object: praw.Reddit):
    submission = reddit_object.submission(url=link)
    title = submission.title
    body_text = submission.selftext
    author = submission.author.name
    return title, body_text, author


# Constructs a string using the title, body, author and top 5 comments of the reddit post
def master_string(title, body, author, comments):
    if body == '[removed]' or body == '[deleted]':
        body = 'Not Available'
    string = f"TITLE OF POST: {title}\nAUTHOR: {author}\nBODY: {body}\nTOP 5 COMMENTS: {comments}"
    return string


# Uses Google's gtts python text to speech tool to output the sound of an inputted string
def say_post(string):
    print(string)
    tts = gTTS(text=string, lang='en')
    tts.save("test.mp3")
    playsound("test.mp3")


# Generates comments and returns them all as a single string
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
        aggregate_string += str(counter + 1)
        aggregate_string += ': '
        aggregate_string += comment.body
        counter += 1
        if counter > 4:
            break
    return aggregate_string


