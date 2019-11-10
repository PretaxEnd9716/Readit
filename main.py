from gtts import gTTS
from tempfile import TemporaryFile
from playsound import playsound
import pyglet
import os
import praw
import string
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
    string = f"TITLE OF POST: {title}\n AUTHOR: {author}\nBODY: {body}\nCOMMENTS: {comments}"
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
        aggregate_string += 'Comment: '
        aggregate_string += comment.body
        counter += 1
        if counter > 4:
            break
    return aggregate_string

def main():
    link = input("Enter in a Reddit post link: ")
    title, body, author = get_data(link, create_reddit_object())
    comments = get_comments(link)
    combined_str = master_string(title, body, author, comments)
    print(combined_str)
    tts = gTTS(text=combined_str, lang='en')
    tts.save("test.mp3")
    playsound("test.mp3")


    #say_post(combined_str)

    #print(get_data(link, create_reddit_object()))
    #print(get_comments(link))


main()
